# Airworthiness Directive (AD) Applicability Extraction & Compliance Evaluation

## Overview

This project provides an **end-to-end automated pipeline** for processing **Airworthiness Directives (ADs)** issued by aviation authorities such as **EASA** and **FAA**.

The system is designed to:

1. **Extract applicability rules** from AD PDF documents using an LLM (Google Gemini).
2. **Normalize and structure** those rules into machine-readable JSON.
3. **Evaluate aircraft compliance** against the extracted AD rules.
4. **Export evaluation results** into a CSV file for easy inspection and reporting.

This project is intended for **research, prototyping, and decision-support** use cases in aviation safety, compliance analysis, and NLP-based regulatory document processing.

---

## Project Workflow

```
AD PDFs
  ↓
[PDF Text Extraction]
  ↓
[LLM-based Rule Parsing]
  ↓
Structured JSON (applicability rules)
  ↓
[Compliance Evaluation Engine]
  ↓
CSV Report (per-aircraft × per-AD status)
```

---

## Repository Structure

```
.
├── .env                    # Environment variables (API keys)
├── .gitignore
├── README.md
├── report.md
├── requirements.txt
│
├── data
│   ├── EASA_AD_2025-0254R1_1.pdf
│   ├── EASA_AD_US-2025-23-53_1.pdf
│   └── extracted_rules.json
│
├── extractor
│   ├── main.py              # Entry point for AD rule extraction
│   ├── config.py            # Configuration & environment loading
│   ├── pdf_utils.py         # PDF text extraction utilities
│   └── llm
│       ├── client.py        # Gemini client wrapper
│       ├── prompt.py        # Prompt templates
│       └── parser.py        # LLM response parsing logic
│
├── eval
│   ├── loader.py            # Load AD rules from JSON
│   ├── evaluator.py         # Core compliance evaluation logic
│   ├── eval_run.py          # Evaluation runner
│   └── ad_compliance_results.csv
```

---

## How to Run

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd <your-repo-name>
```

---

### 2. Create and Configure `.env`

Create a `.env` file in the project root:

```
GOOGLE_API_KEY=your_google_gemini_api_key_here
```

> The project uses **Google Gemini (GenAI SDK)** for rule extraction.

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Extract AD Applicability Rules

Place AD PDF files inside the `data/` folder, then run:

```bash
python extractor/main.py
```

This will:

- Read all PDFs in `data/`
- Extract applicability rules using the LLM
- Save structured output to:

```
data/extracted_rules.json
```

---

### 5. Run Compliance Evaluation

Execute the evaluation pipeline:

```bash
python eval/eval_run.py
```

This will:

- Load `extracted_rules.json`
- Compare each aircraft against each AD
- Generate a CSV report:

```
eval/ad_compliance_results.csv
```

---

## Output Format

The CSV output follows this structure:

| Aircraft | MSN  | Modifications | FAA AD 2025-23-53 | EASA AD 2025-0254R1 |
| -------- | ---- | ------------- | ----------------- | ------------------- |
| A320-214 | 4500 | None          | Affected          | Not affected        |

Each cell indicates the **applicability status** of a specific AD for a given aircraft.

---

## Notes & Disclaimer

- This system **does not replace official regulatory compliance processes**.
- LLM outputs should always be **validated by domain experts**.
- AD texts may contain ambiguities that require manual interpretation.

---

## Future Improvements

- Support for additional aviation authorities
- Rule confidence scoring
- Enhanced MSN constraint parsing
- Web-based visualization dashboard

---
