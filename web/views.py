from flask import render_template
from app import app, pages
import json

@app.route('/')
def home():
    with open('data/galeria.json', encoding='utf8') as data_file:    
        galeria = json.load(data_file)
    
    return render_template('index.html', galeria=galeria)
