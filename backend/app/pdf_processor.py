import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    """
    Extracts text content from a PDF file.

    Args:
        pdf_path (str): The path to the PDF file.

    Returns:
        str: The extracted text content as a single string.  Returns an empty string on error.
    """
    text = ""
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text() + "\n" # Add newline for better formatting
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {e}")
        return "" # Or raise the exception if you prefer to handle it differently

    return text

# Example usage (for testing):
if __name__ == "__main__":
    pdf_file_path = "uploads/llm.pdf"  # Replace with your PDF file
    extracted_text = extract_text_from_pdf(pdf_file_path)

    if extracted_text:
        print("Extracted Text:")
        print(extracted_text[:500] + "...")  # Print only the first 500 characters for brevity
    else:
        print("No text extracted or an error occurred.")