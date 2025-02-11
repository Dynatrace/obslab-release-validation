--8<-- "snippets/bizevent-enable-change.js"

A product manager informs you that they're ready to release their new feature. They ask you to enable the feature and run the load test in a dev environment.

They tell you that the new feature is behind a flag called `paymentServiceFailure` (yes, an obvious name for this demo) and they tell you to change the `defaultValue` from `off` to `on`.

## Update the Feature Flag and Inform Dynatrce

Run the following script which notifies Dynatrace using a `CUSTOM_INFO` event of the change inc. the new value.

```
./runtimeChange.sh paymentServiceFailure on
```

## Change Flag Value

Locate the `flags.yaml` file.
Change the `defaultValue` of the `paymentServiceFailure` flag from `"off"` to `"on"` (line `84`).

Apply those changes:

```
kubectl apply -f $CODESPACE_VSCODE_FOLDER/flags.yaml
```

You should see:

```
configmap/my-otel-demo-flagd-config configured
```

## Run Acceptance Load Test

It is time to run an acceptance load test to see if the new feature has caused a regression.

This load test will run for 3 minutes and then trigger the site reliability guardian again:

```
kubectl apply -f .devcontainer/k6/k6-after-change.yaml
```

## Configuration Change Events

While you are waiting for the load test to complete, it is worth noting that each time a feature flag is changed, you should execute `runtimeChange.sh` shell script to send an event to the service that is affected.

The feature flag changes the behaviour of the `paymentservice` (which the `checkoutservice` depends on).

Look at the `paymentservice` and notice the configuration changed events.

!!! tip
    You can send event for anything you like: deployments, load tests, security scans, configuration changes and more.

![payment service event](images/paymentservice-event.png)


<div class="grid cards" markdown>
- [Click Here to Continue:octicons-arrow-right-24:](view-acceptance-test-results.md)
</div>