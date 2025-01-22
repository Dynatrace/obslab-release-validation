## Dynatrace Details

### Environment ID

Make a note of your Dynatrace environment ID.

The generic format is:

```
https://<EnvironmentID>.apps.dynatrace.com
```

So the environment ID would be `abc12345` for this URL:

```
https://abc12345.apps.dynatrace.com
```

### Environment

!!! tip "Unsure?"
    If you are unsure, just use the word `live`

You may be running in an environment other than `live`. You can see this by the URL structure.

| URL structure                              | Example                             | Environment |
|----------------------------------------------------------|-----------------------|-------------|
| `https://<EnvironmentID>.apps.dynatrace.com` | https://abc12345.apps.dynatrace.com |  `live`     |
| `https://<EnvironmentID>.sprint.dynatracelabs.com` | https://abc12345.sprint.dynatracelabs.com |  `sprint`     |

!!! success "Save the info"
    You should now have 2 pieces of info:
    
    * Environment ID: `abc12345`
    * Environment: `live`