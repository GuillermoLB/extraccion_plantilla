import os
import spacy

# Load the Spanish NLP model
nlp = spacy.load("es_core_news_sm")

def extract_information(text):
    doc = nlp(text)
    name = None
    date = None
    location = None
    
    # Extract named entities for person (name), date, and location
    for ent in doc.ents:
        if ent.label_ == "PER":
            name = ent.text
        elif ent.label_ == "LOC":
            location = ent.text
        elif ent.label_ == "DATE":
            date = ent.text

    return {
        'name': name,
        'date': date,
        'location': location
    }

def generar_documento(informacion):
    # Path to the template
    template_path = '/app/template.txt'
    
    # Load the template
    with open(template_path, 'r') as file:
        template = file.read()
    
    # Replace placeholders with actual information
    document_text = template.format(
        name=informacion['name'] or 'N/A',
        date=informacion['date'] or 'N/A',
        location=informacion['location'] or 'N/A'
    )
    
    # Save the generated document
    output_path = '/app/generated_document.txt'
    with open(output_path, 'w') as file:
        file.write(document_text)
    
    return output_path
