def evaluate_ad_for_aircraft(aircraft: dict, ad_rule: dict) -> str:
    model = aircraft["model"].lower().strip()
    mods = [m.lower().strip() for m in aircraft["modifications"]]

    # 1. Applicability check
    if model not in ad_rule["aircraft_models"]:
        return "❌ Not applicable"

    # 2. Exclusion check
    for mod in mods:
        for excluded in ad_rule["excluded_if_modifications"]:
            if excluded in mod:
                return "❌ Not affected"

    return "✅ Affected"
