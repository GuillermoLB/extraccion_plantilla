import os
from flask import Blueprint, request, send_file, render_template
from .utils import generar_documento, extract_information

app = Blueprint('app', __name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        
        if file:
            # Ensure the uploads directory exists
            uploads_dir = '/app/uploads'
            if not os.path.exists(uploads_dir):
                os.makedirs(uploads_dir)
            
            # Save the uploaded file
            file_path = os.path.join(uploads_dir, file.filename)
            file.save(file_path)
            
            # Read the content of the uploaded file
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
            
            # Extract information using NLP
            informacion_extraida = extract_information(text)

            # Generate the document using the template
            generated_file_path = generar_documento(informacion_extraida)
            
            # Return the generated document to the user
            return send_file(generated_file_path, as_attachment=True)

    return render_template('upload.html')
