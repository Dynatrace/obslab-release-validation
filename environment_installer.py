import os
from utils import *

OTEL_DEMO_VERSION="0.33.4"

# if (
#     DT_API_TOKEN is None or
#     DT_ENVIRONMENT_ID is None or
#     DT_ENVIRONMENT_TYPE is None
# ):
#     exit("Missing mandatory environment variables. Cannot proceed. Exiting.")

# # Build DT environment URLs
DT_TENANT_APPS, DT_TENANT_LIVE = build_dt_urls(dt_env_id=DT_ENVIRONMENT_ID, dt_env_type=DT_ENVIRONMENT_TYPE)

# # Delete cluster first, in case this is a re-run
# logger.info("Deleting any previous cluster")
# run_command(["kind", "delete", "cluster"])

# Find and replace placeholders
# Commit up to repo
# Find and replace DT_TENANT_LIVE_PLACEHOLDER with real text
# eg. "https://abc12345.live.dynatrace.com"
# Push = False for the first set
# because we push on the final git commit

logger.info("Doing file replacements...")
# Replace placeholders in helm-values.yaml with realtime values
do_file_replace(pattern=".devcontainer/otel-demo/helm-values.yaml", find_string="CODESPACE_NAME_PLACEHOLDER", replace_string=CODESPACE_NAME, recursive=False)
do_file_replace(pattern=".devcontainer/otel-demo/helm-values.yaml", find_string="GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN_PLACEHOLDER", replace_string=GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN, recursive=False)
# Replace placeholders in k6 Kubernetes YAML with realtime values
do_file_replace(pattern=".devcontainer/k6/k6.yaml", find_string="CODESPACE_NAME_PLACEHOLDER", replace_string=CODESPACE_NAME, recursive=False)
do_file_replace(pattern=".devcontainer/k6/k6.yaml", find_string="GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN_PLACEHOLDER", replace_string=GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN, recursive=False)
# Replace placeholders in k6 Kubernetes YAML with realtime values
do_file_replace(pattern=".devcontainer/k6/k6-load-test-script.yaml", find_string="CODESPACE_NAME_PLACEHOLDER", replace_string=CODESPACE_NAME, recursive=False)
do_file_replace(pattern=".devcontainer/k6/k6-load-test-script.yaml", find_string="GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN_PLACEHOLDER", replace_string=GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN, recursive=False)
# Replace placeholders in k6 Kubernetes YAML with realtime values
do_file_replace(pattern=".devcontainer/k6/k6-after-change.yaml", find_string="CODESPACE_NAME_PLACEHOLDER", replace_string=CODESPACE_NAME, recursive=False)
do_file_replace(pattern=".devcontainer/k6/k6-after-change.yaml", find_string="GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN_PLACEHOLDER", replace_string=GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN, recursive=False)
# Replace placeholders in runtimeChange with realtime values
do_file_replace(pattern="runtimeChange.sh", find_string="DT_ENDPOINT_PLACEHOLDER", replace_string=DT_TENANT_LIVE)

# Create cluster
logger.info("Creating new cluster")
run_command(["kind", "create", "cluster", "--config", ".devcontainer/kind-cluster.yaml", "--wait", STANDARD_TIMEOUT])

logger.info("Creating secret")
run_command(["kubectl", "create", "secret", "generic" ,"dt-details", f"--from-literal=DT_ENDPOINT={DT_TENANT_LIVE}", f"--from-literal=DT_API_TOKEN={DT_API_TOKEN}"])

logger.info("Adding helm repo")
run_command(["helm", "repo", "add", "open-telemetry", "https://open-telemetry.github.io/opentelemetry-helm-charts"])
run_command(["helm", "repo", "update"])

logger.info("Installing otel demo")
output = run_command(["helm", "install", "my-otel-demo", "open-telemetry/opentelemetry-demo", "--values=.devcontainer/otel-demo/helm-values.yaml", f"--version={OTEL_DEMO_VERSION}"])

# send_startup_ping(demo_name="obslab-testing")