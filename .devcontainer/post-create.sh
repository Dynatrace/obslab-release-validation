#!/bin/bash

# CREATE_CLUSTER_WAIT=300s
# OTEL_DEMO_VERSION=0.33.4

# # 1. Install Python, gh CLI and test harness dependencies
# sudo apt install gh -y
# sudo apt install -y python3
# sudo apt install -y python3-pip
# pip install --break-system-packages -r requirements.txt

# Install and configure cluster
# python3 cluster_installer.py

####################################
# Note:
# The following are "magic" env vars, set automatically by GitHub
# - $CODESPACE_NAME
# - $GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN
#
# The following are set as env vars when the user enters their "secret values" via the form when they spin up the codespace
# - $DT_ENVIRONMENT_ID
# - $DT_ENVIRONMENT_TYPE
# - $DT_API_TOKEN_OBSLAB_RELEASE_VALIDATION
#
# Use `printenv` to see all env vars.
####################################

# Replace placeholders in helm-values.yaml with realtime values
#sed -i "s,CODESPACE_NAME_PLACEHOLDER,$CODESPACE_NAME," .devcontainer/otel-demo/helm-values.yaml
#sed -i "s,GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN_PLACEHOLDER,$GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN," .devcontainer/otel-demo/helm-values.yaml
# Replace placeholders in k6 Kubernetes YAML with realtime values
#sed -i "s,CODESPACE_NAME_PLACEHOLDER,$CODESPACE_NAME," .devcontainer/k6/k6.yaml
#sed -i "s,GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN_PLACEHOLDER,$GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN," .devcontainer/k6/k6.yaml
# Replace placeholders in k6 Kubernetes YAML with realtime values
#sed -i "s,CODESPACE_NAME_PLACEHOLDER,$CODESPACE_NAME," .devcontainer/k6/k6-load-test-script.yaml
#sed -i "s,GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN_PLACEHOLDER,$GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN," .devcontainer/k6/k6-load-test-script.yaml
# Replace placeholders in k6 Kubernetes YAML with realtime values
#sed -i "s,CODESPACE_NAME_PLACEHOLDER,$CODESPACE_NAME," .devcontainer/k6/k6-after-change.yaml
#sed -i "s,GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN_PLACEHOLDER,$GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN," .devcontainer/k6/k6-after-change.yaml

# Create Cluster
#kind create cluster --config .devcontainer/kind-cluster.yaml --wait $CREATE_CLUSTER_WAIT

# Store DT Details in a secret (used by OTEL collector for data ingest)
#kubectl create secret generic dt-details --from-literal=DT_ENDPOINT_OBSLAB_RELEASE_VALIDATION=$DT_ENDPOINT_OBSLAB_RELEASE_VALIDATION --from-literal=DT_API_TOKEN_OBSLAB_RELEASE_VALIDATION=$DT_API_TOKEN_OBSLAB_RELEASE_VALIDATION

# Add OTEL demo using Helm
#helm repo add open-telemetry https://open-telemetry.github.io/opentelemetry-helm-charts
#helm repo update
#helm install my-otel-demo open-telemetry/opentelemetry-demo --values .devcontainer/otel-demo/helm-values.yaml --version $OTEL_DEMO_VERSION

# Creation Ping
# curl -X POST https://grzxx1q7wd.execute-api.us-east-1.amazonaws.com/default/codespace-tracker \
#   -H "Content-Type: application/json" \
#   -d "{
#     \"tenant\": \"$DT_ENDPOINT_OBSLAB_RELEASE_VALIDATION\",
#     \"repo\": \"$GITHUB_REPOSITORY\",
#     \"demo\": \"obslab-release-validation\",
#     \"codespace.name\": \"$CODESPACE_NAME\"
#   }"