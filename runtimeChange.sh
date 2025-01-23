#!/bin/bash
# Usage: ./runtimeChange.sh flagKey newFlagValue remediationValueIfFailure
# eg. ./runtimeChange.sh paymentServiceFailure on

echo "Changing feature flag key: $1 to $2"

##############
# Step 1
# Inform Dynatrace that a configuration change is occurring
##############
curl -X POST "DT_ENDPOINT_PLACEHOLDER/api/v2/events/ingest" \
  -H "accept: application/json; charset=utf-8" -H "Authorization: Api-Token $DT_API_TOKEN" -H "Content-Type: application/json; charset=utf-8" \
  -d "{
  \"title\": \"featureflag change\",
  \"entitySelector\": \"type(SERVICE),entityName.equals(paymentservice)\",
  \"eventType\": \"CUSTOM_INFO\",
  \"timeout\": 1,
  \"properties\": {
    \"type\": \"configuration_change\",
    \"feature_flag.key\": \"$1\",
    \"defaultValue\": \"$2\"
  }
}"

##############
# Step 2
# Change the $1 feature flag key to the value of $2
# This is messy (and in reality would be handled with a proper GitOps process eg. Pull Requests and a tool like ArgoCD)
# 1. Read flags.yaml with yq
# 2. Get the JSON flag values from .data and pass to jq
# 3. jq changes the defaultValue
# 4. This is saved as an environment variable RESULT
# 5. Add a pipe and newline to result and use yq to edit flags.yaml inplace
# 6. kubectl apply the changed file
##############
RESULT=$(yq '.data["demo.flagd.json"]' .devcontainer/otel-demo/flags.yaml | yq ".flags.$1.defaultVariant = \"$2\"")
res=$RESULT yq -i '.data["demo.flagd.json"] = env(res)' .devcontainer/otel-demo/flags.yaml
sed -i 's/  demo.flagd.json: /  demo.flagd.json: |\n    /g' .devcontainer/otel-demo/flags.yaml

# Apply changes
kubectl apply -f .devcontainer/otel-demo/flags.yaml

echo "flag: $1 property: defaultVariant set to value: $2"