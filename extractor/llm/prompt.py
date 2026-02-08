def build_prompt(ad_text: str) -> str:
    return f"""
Extract the document identifier (AD ID) and applicability rules from this Airworthiness Directive (AD).

IMPORTANT RULES FOR AD ID:
- Use the official identifier exactly as written.
- Include the issuing authority ONLY if it is part of the identifier itself.
- Do NOT prepend or infer authority names.

IMPORTANT RULES FOR AIRCRAFT MODELS:
- Extract ONLY aircraft model designators (technical model codes).
- DO NOT include manufacturer names or family names.

General Rules:
- Output ONLY valid JSON
- Do NOT include markdown
- Do NOT add explanations

JSON schema:
{{
  "ad_id": "string",
  "applicability_rules": {{
    "aircraft_models": ["string"],
    "msn_constraints": "string or null",
    "excluded_if_modifications": ["string"],
    "required_modifications": ["string"]
  }}
}}

AD Text:
\"\"\"
{ad_text}
\"\"\"
"""
