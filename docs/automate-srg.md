# Automate the Site Reliability Guardian

--8<-- "snippets/bizevent-automate-srg.js"

[Site reliability guardians](https://docs.dynatrace.com/docs/platform-modules/automations/site-reliability-guardian){target="_blank"} can be automated so they happen whenever you prefer (on demand / on schedule / event based). A [Dynatrace workflow](https://docs.dynatrace.com/docs/platform-modules/automations/workflows){target="_blank"} is used to achieve this.

In this demo:

* A load test will run and send a "load test finished" Software Delivery Lifecycle event into Dynatrace (see below).
* A Dynatrace workflow will react to that event and trigger a guardian.

Let's plumb that together now.

!!! info "Sample k6 teardown test finished event"

    For information only, no action is required.
    
    This is already coded into the [demo load test script](https://github.com/dynatrace/obslab-release-validation/blob/main/.devcontainer/k6/k6-load-test-script.yaml#L38){target="_blank"}.

    ```javascript
    export function teardown() {
        // Send event at the end of the test
        let payload = {
          "entitySelector": "type(SERVICE),entityName.equals(checkoutservice)",
          "eventType": "CUSTOM_INFO",
          "properties": {
            "tool": "k6",
            "action": "test",
            "state": "finished",
            "purpose": `${__ENV.LOAD_TEST_PURPOSE}`,
            "duration": test_duration
          },
          "title": "k6 load test finished"
        }
      
        let res = http.post(`${__ENV.K6_DYNATRACE_URL}/api/v2/events/ingest`, JSON.stringify(payload), post_params);
      }
    }
    ```

## Create a Workflow to Trigger Guardian

Ensure you are still on the `Three golden signals (checkoutservice)` screen.

* Click the `Automate` button. This will create a template workflow.
* Change the `event type` from `bizevents` to `events`.
* Change the `Filter query` to:

```
event.type == "CUSTOM_INFO" and
dt.entity.service.name == "checkoutservice" and
tool == "k6" and
action == "test" and
state == "finished"
```

* Click the `run_validation` node.
* Remove `event.timeframe.from` and replace with:

{% raw %}
```
now-{{ event()['duration'] }}
```
{% endraw %}

The UI will change this to `now-event.duration`.

* Remove `event.timeframe.to` and replace with:
```
now
```

* Click the `Save` button.

## Workflow Created

The workflow is now created and connected to the guardian. It will be triggered whenever the platform receives an event like below.

![dynatrace automate SRG button](images/dt-srg-screen-6.png)
![dynatrace workflow trigger 1](images/dt-workflow-screen-1.png)
![dynatrace workflow time selector 2](images/dt-workflow-screen-2.png)

The workflow is now live and listening for events.

<div class="grid cards" markdown>
- [Click Here to Continue:octicons-arrow-right-24:](enable-auto-baselines.md)
</div>