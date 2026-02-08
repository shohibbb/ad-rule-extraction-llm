import json

# Helper function to normalize text for consistent comparisons
def normalize(text):
    return text.lower().strip()

# Load AD rules from a JSON file and structure them for evaluation
def load_ad_rules(json_path: str) -> dict:
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if isinstance(data, dict):
        data = [data]

    rules = {}

    for ad in data:
        ad_id = ad.get("ad_id")
        app = ad.get("applicability_rules", {})

        if not ad_id or not app:
            continue

        rules[ad_id] = {
            "aircraft_models": [normalize(m) for m in app.get("aircraft_models", [])],
            "msn_constraints": app.get("msn_constraints"),
            "excluded_if_modifications": [
                normalize(m) for m in app.get("excluded_if_modifications", [])
            ],
        }

    return rules
