--8<-- "snippets/bizevent-view-acceptance-test-results.js"

## View Data

Wait for all jobs to complete:

```
kubectl -n default wait --for=condition=Complete --all --timeout 120s jobs
```

All jobs (including the `acceptance-load-test`) should now be `Complete`.

Refresh the Site Reliability Guardian results heatmap again and notice that the guardian has failed.

![srg acceptance test failed](images/dt-srg-acceptance-test-failed.png)

The guardian has failed due to the error rate being too high.

![checkoutservice error rate too high](images/dt-srg-checkoutservice-error-rate-too-high.png)

Navigating to the `checkoutservice` (`ctrl + k` > `services` > `checkoutservice`), you can see the increase in failure rate.

![services screen increased error rate on checkoutservice](images/dt-services-checkoutservice-increased-error-rate.png)

Scroll down the services screen until you see the OpenTelemetry traces list. Notice lots of failed requests:

![checkoutservice failed traces](images/dt-services-checkoutservice-distributed-trace-failures.png)

## Analyse a Failed Request

![failed trace](images/dt-distributed-traces-checkoutservice-failed.png)

Drill into one of the failed requests and notice lots of failures.

These failures are bubbling up through the request chain back towards the checkoutservice.

Ultimately though, the failure comes from the final span in the trace: The call to `PaymentService/Charge`.

Investigating the span events the cause of the failure becomes clear: The payment service cuase an exception. The exception message and stacktrace is given:

```
exception.message	PaymentService Fail Feature Flag Enabled
exception.stacktrace	Error: PaymentService Fail Feature Flag Enabled at module.exports.charge
  (/usr/src/app/charge.js:21:11) at process.processTicksAndRejections
  (node:internal/process/task_queues:95:5) at async Object.chargeServiceHandler
  [as charge] (/usr/src/app/index.js:21:22)
exception.type	Error
```

![root cause: payment service](images/dt-span-root-cause-paymentservice.png)


## Roll Back Change

Inform Dynatrace that a change in configuration is coming.
The `paymentServiceFailure` flag will be set to `off`

```
./runtimeChange.sh paymentServiceFailure off
```

Again edit `flags.yaml` and set the `defaultValue` of `paymentServiceFailure` from `"on"` to `"off"` (line `84`)

Apply the changes:

```
kubectl apply -f $CODESPACE_VSCODE_FOLDER/flags.yaml
```

## Summary

Looking back at the initial brief, it was your job to:

* Enable a feature flag in a development environment.
* Judge the impact (if any) of that change on the application.
* If an impact is observed, gather the evidence and then disable the feature flag.
* Make the "go / no go" decision for that feature.
* Provide feedback to the product managers on why you made the decision you did.

So how did things turn out?

* You have enabled a feature flag and send contextual event information to Dynatrace.
* You used OpenTelemetry and Dynatrace to make an evidence-based analysis of the new software quality.
* You have automated the change analysis, noticing an impact and remediated it.
* You have protected users by automating this analysis in a development environment (of course, you could repeat this setup in production too).
* You have made the `no go` decision based on evidence provided by OpenTelemetry and the Dynatrace Site Reliability Guardian.
* You can provide this evidence (down to the stacktrace and line of code) back to the product manager so they can prioritise fixes.

!!! hint "Works with any metric"
    The techniques described here work with any metric, from any source.

    You are encouraged to use metrics from other devices and sources (such as business related metrics like revenue).

!!! success
    The Dynatrace Platform, Site Reliability Guardian and Workflows have provided visibility and automated change analysis.



<div class="grid cards" markdown>
- [Cleanup Resources :octicons-arrow-right-24:](cleanup.md)
</div>