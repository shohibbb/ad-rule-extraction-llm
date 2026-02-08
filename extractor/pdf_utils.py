from pypdf import PdfReader


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract plain text from all pages of a PDF file.

    Args:
        pdf_path (str): Filesystem path to the PDF file.

    Returns:
        str: Concatenated text from all pages, separated by newlines,
             with leading/trailing whitespace removed.
    """
    # Create a PdfReader for the given file path (opens and parses the PDF).
    reader = PdfReader(pdf_path)

    # Collect text from each page in this list.
    pages = []

    # Iterate over each page object in the PDF.
    for page in reader.pages:
        # Use pypdf's page.extract_text() to get the page's textual content.
        text = page.extract_text()
        # Only append if text was successfully extracted (None check).
        if text:
            pages.append(text)

    # Join all page texts with newlines and strip outer whitespace before returning.
    return "\n".join(pages).strip()