# Getting Started

You must have the following to use this hands on demo.

* A Dynatrace environment ([sign up here](https://dt-url.net/trial){target="_blank"})
* A Dynatrace API token (see below)

Save the Dynatrace environment URL **without** the trailing slash and without the `.apps.` in the URL:

```
https://abc12345.live.dynatrace.com
```

### Create API Token
In Dynatrace:

* Press `ctrl + k`. Search for `access tokens`.
* Create a new access token with the following permissions:
    * `metrics.ingest`
    * `logs.ingest`
    * `openTelemetryTrace.ingest`
    * `openpipeline.events_sdlc`

## Start Demo

Click this button to open the demo environment. This will open in a new tab.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/dynatrace-perfclinics/obslab-release-validation){target="_blank"}

## [Click Here to Continue...](validate-telemetry.md)