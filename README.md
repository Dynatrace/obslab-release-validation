# Observability Lab: Release Validation

In this demo, you take on the role of a Product Manager or DevOps engineer. You are running an application, and wish to enable a new feature.

The application is already instrumented to emit tracing data, using the OpenTelemetry standard. The demo system will be automatically configured to transport that data to Dynatrace for storage and processing.

Your job is to:

- Ensure each service in the application is healthy.
- Ensure that any new release of a microservice does not negatively impact the application.

To achieve these objectives, you will:

- Create a Site Reliability Guardian to test and ensure the health of your microservices (starting with the most user impacting service - the checkoutservice)
- Use the auto baselining capability of Dynatrace to suggest (and dynamically adjust) thresholds based on current and past performance.

## Watch Overview Video on YouTube

Click the image below to watch the overview video on YouTube:

[![Validate Software Releases with Dynatrace Overview Video](https://img.youtube.com/vi/91t_NWnTFWA/0.jpg)](https://www.youtube.com/watch?v=91t_NWnTFWA)

## [Start the hands-on here >>](https://dynatrace.github.io/obslab-release-validation/)
