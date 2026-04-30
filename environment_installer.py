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

# Replace placeholders in runtimeChange with realtime values
do_file_replace(pattern="runtimeChange.sh", find_string="DT_ENDPOINT_PLACEHOLDER", replace_string=DT_TENANT_LIVE)

# This logic essentially runs `kind create cluster`
createKubernetesCluster()

addHelmChart(name="open-telemetry", url="https://open-telemetry.github.io/opentelemetry-helm-charts", update=True)

run_command(["kubectl", "create", "secret", "generic" ,"dt-details", f"--from-literal=DT_ENDPOINT={DT_TENANT_LIVE}", f"--from-literal=DT_API_TOKEN={DT_API_TOKEN}"])

logger.info("Installing otel demo")
installOTELDemoApp()