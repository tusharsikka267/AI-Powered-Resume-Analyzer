import fitz  # PyMuPDF
import spacy

nlp = spacy.load("en_core_web_sm")

def parse_resume_pdf(path: str) -> dict:
    """Extracts raw text from a PDF resume and returns a dict with text & rough skill tokens."""
    doc = fitz.open(path)
    text = " ".join(page.get_text() for page in doc)
    doc.close()

    doc_nlp = nlp(text)
    noun_chunks = [chunk.text.strip().lower() for chunk in doc_nlp.noun_chunks]
    skills = list(set(noun_chunks))
    return { "text": text, "skills": skills }
