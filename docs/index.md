# Release Validation for SREs with Site Reliability Guardian

In this demo, you take on the role of a Site Reliability Engineer (SRE). You are running an application, consisting of a number of microservices.

The application is already instrumented to emit tracing data, using the [OpenTelemetry](https://opentelemetry.io){target="_blank"} standard. The demo system will be automatically configured to transport that data to Dynatrace for storage and processing.

Your job is to:

* Ensure each service in the application is healthy.
* Ensure that any new release of a microservice does not negatively impact the application.

To achieve these objectives, you will:

* Create a Site Reliability Guardian to test and ensure the health of your microservices (starting with the most user impacting service - the `checkoutservice`)
* Use the auto baselining capability of Dynatrace to suggest (and dynamically adjust) thresholds based on current and past performance.

## A New Release

Your company utilises feature flags to enable new features. A product manager informs you that they wish to release a new feature.

It is your job to:

* Enable that feature flag in a development environment.
* Judge the impact (if any) of that change on the application.
* If an impact is observed, gather the evidence and then disable the feature flag.
* Make the "go / no go" decision for that feature.
* Provide feedback to the product managers on why you made the decision you did.

## Compatibility

| Deployment         | Tutorial Compatible |
|--------------------|---------------------|
| Dynatrace Managed  | ❌                 |
| Dynatrace SaaS     | ✔️                 |

<div class="grid cards" markdown>
- [Click Here to Begin :octicons-arrow-right-24:](getting-started.md)
</div>