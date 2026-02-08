from loader import load_ad_rules
from evaluator import evaluate_ad_for_aircraft
import csv
import os

# Sample aircraft data for evaluation got from the task instructions
AIRCRAFT_DATA = [
    {"model": "MD-11F", "msn": 48400, "modifications": []},
    {"model": "A320-214", "msn": 4500, "modifications": ["mod 24591 (production)"]},
    {"model": "A320-214", "msn": 4500, "modifications": []},
    {"model": "MD-11", "msn": 48123, "modifications": []},
    {"model": "DC-10-30F", "msn": 47890, "modifications": []},
    {"model": "Boeing 737-800", "msn": 30123, "modifications": []},
    {"model": "A320-214", "msn": 5234, "modifications": []},
    {"model": "A320-232", "msn": 6789, "modifications": ["mod 24591 (production)"]},
    {"model": "A320-214", "msn": 7456, "modifications": ["SB A320-57-1089 Rev 04"]},
    {"model": "A321-111", "msn": 8123, "modifications": []},
    {"model": "A321-112", "msn": 364, "modifications": ["mod 24977 (production)"]},
    {"model": "A319-100", "msn": 9234, "modifications": []},
    {"model": "MD-10-10F", "msn": 46234, "modifications": []},
]

# Export evaluation results to a CSV file
def export_results_to_csv(results, ad_ids, output_path):
    headers = ["Aircraft", "MSN", "Modifications"] + ad_ids

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()

        for row in results:
            writer.writerow(row)


# Main evaluation routine 
def main():
    ad_rules = load_ad_rules("data\\extracted_rules.json")
    ad_ids = list(ad_rules.keys())

    print("\n=== AIRWORTHINESS DIRECTIVE COMPLIANCE CHECK ===\n")

    all_rows = []

    for ac in AIRCRAFT_DATA:
        print(
            f"Aircraft: {ac['model']} | MSN: {ac['msn']} | "
            f"Mods: {', '.join(ac['modifications']) or 'None'}"
        )

        row = {
            "Aircraft": ac["model"],
            "MSN": ac["msn"],
            "Modifications": ", ".join(ac["modifications"]) or "None",
        }

        for ad_id, ad_rule in ad_rules.items():
            status = evaluate_ad_for_aircraft(ac, ad_rule)
            row[ad_id] = status
            print(f"  {ad_id}: {status}")

        all_rows.append(row)
        print("-" * 50)

    output_csv = os.path.join("eval", "ad_compliance_results.csv")
    export_results_to_csv(all_rows, ad_ids, output_csv)

    print(f"\n✅ Results exported to: {output_csv}")


if __name__ == "__main__":
    main()
