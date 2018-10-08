from flask import render_template
from app import app, pages
import json
import io

@app.route('/')
def home():
    with io.open('data/galeria.json', encoding='utf8') as data_file:    
        galeria = json.load(data_file)
    
    with io.open('data/investigaciones.json', encoding='utf8') as data_file:    
        investigaciones = json.load(data_file)
    
    return render_template('index.html', galeria=galeria, investigaciones=investigaciones[:(4 - len(investigaciones))])

@app.route('/investigaciones/')
def investigaciones():
    
    with io.open('data/investigaciones.json', encoding='utf8') as data_file:    
        investigaciones = json.load(data_file)
    
    return render_template('investigaciones.html', investigaciones=investigaciones)

@app.route('/documentoslegales/')
def documentoslegales():
    
    with io.open('data/documentoslegales.json', encoding='utf8') as data_file:    
        documentoslegales = json.load(data_file)
    
    return render_template('documentoslegales.html', documentoslegales=documentoslegales)