import json
import os

def write_event_metric(event_type, reference_id, intensity, details):
    metric = {
        "event_type": event_type,
        "reference_id": reference_id,
        "intensity": intensity,
        "timestamp": str(details.get("timestamp")),
        "extra_info": details
    }

    if not os.path.exists("metrics"):
        os.makedirs("metrics")

    with open(f"metrics/event_{reference_id}.json", "w") as f:
        json.dump(metric, f, indent=4)
