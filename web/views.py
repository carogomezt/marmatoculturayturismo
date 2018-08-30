from flask import render_template
from app import app, pages
import json

@app.route('/')
def home():
    with open('data/galeria.json', encoding='utf8') as data_file:    
        galeria = json.load(data_file)
    
    with open('data/investigaciones.json', encoding='utf8') as data_file:    
        investigaciones = json.load(data_file)
    
    return render_template('index.html', galeria=galeria, investigaciones=investigaciones[:(4 - len(investigaciones))])

@app.route('/investigaciones/')
def investigaciones():
    
    with open('data/investigaciones.json', encoding='utf8') as data_file:    
        investigaciones = json.load(data_file)
    
    return render_template('investigaciones.html', investigaciones=investigaciones)