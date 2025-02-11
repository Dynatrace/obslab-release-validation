# Getting Started

--8<-- "snippets/bizevent-getting-started.js"

You must have the following to use this hands on demo.

* A Dynatrace environment ([sign up here](https://dt-url.net/trial){target="_blank"})
* A Dynatrace API token (see below)

--8<-- "snippets/tenant-details.md"

### Create API Token
In Dynatrace:

* Press `ctrl + k`. Search for `access tokens`.
* Create a new access token with the following permissions:
    * `metrics.ingest`
    * `logs.ingest`
    * `events.ingest`
    * `openTelemetryTrace.ingest`

--8<-- "snippets/save-info-final.md"

## Start Demo

--8<-- "snippets/codespace-details-warning-box.md"

Click this button to open the demo environment. This will open in a new tab.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/dynatrace/obslab-release-validation){target="_blank"}

<div class="grid cards" markdown>
- [Click Here to Continue :octicons-arrow-right-24:](validate-telemetry.md)
</div>