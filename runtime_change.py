import requests
from dotenv import load_dotenv
import os

load_dotenv()

DT_URL = os.environ.get("DT_URL", "")
DT_API_TOKEN = os.environ.get("DT_API_TOKEN", "")
DT_ENDPOINT = f"{DT_URL}/api/v2/events/ingest"

headers = {
    "Content-Type": "application/json; charset=utf-8",
    "accept": "application/json; charset=utf-8",
    "Authorization": f"Api-Token {DT_API_TOKEN}"
}
payload = {
    "title": "feature flag changed",
    "entitySelector": "type(SERVICE),entityName.equals(payment)",
    "eventType": "CUSTOM_INFO",
    "timeout": 1,
    "properties": {
        "type": "configuration_change",
        "feature_flag.key": "paymentFailure",
        "defaultValue": "on",
        "dt.event.is_rootcause_relevant": True
    }
}

resp = requests.post(
    url=DT_ENDPOINT,
    headers=headers,
    json=payload
)

print(resp.status_code)