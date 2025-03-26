from app.pdf_processor import extract_text_from_pdf

pdf_path = "uploads/llm.pdf"
extracted_text = extract_text_from_pdf(pdf_path)
print(extracted_text)  # Check if the text is extracted correctly
