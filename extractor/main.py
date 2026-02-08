import glob
import json
import os

from pdf_utils import extract_text_from_pdf
from llm.parser import parse_ad_with_llm


# run_pipeline: scan a folder for PDF files, extract text from each PDF,
# parse the extracted text with the LLM parser, collect results, and save
# save as a JSON file in the same folder.
def run_pipeline(folder_path: str):
    # Find all PDF files in the provided folder_path
    pdf_files = glob.glob(os.path.join(folder_path, "*.pdf"))
    results = []

    for pdf_path in pdf_files:
        # Process each PDF path found
        print(f"Processing: {pdf_path}")

        try:
            # Extract plain text from the PDF file
            text = extract_text_from_pdf(pdf_path)
            # Parse the extracted text into structured AD/rule data using the LLM parser
            parsed = parse_ad_with_llm(text)
            # Collect parsed output for later saving
            results.append(parsed)

        except Exception as e:
            # Log failures and continue processing remaining files
            print(f"Failed on {pdf_path}: {e}")

    # Save all collected parsed results to extracted_rules.json in the folder
    output_path = os.path.join(folder_path, "extracted_rules.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)

    print(f"Saved to {output_path}")


# If this module is executed directly, run the pipeline on the default "data" folder.
if __name__ == "__main__":
    run_pipeline("data")