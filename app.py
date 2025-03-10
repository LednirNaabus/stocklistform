import os
import flask
from flask import Flask, render_template, request, redirect
from google_sheets import append_to_sheet

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/submit", methods=['POST'])
def submit():
    values = []
    categories = [
        'Oil', 'Oil Filter', 'Cabin Filter', 'Air Filter', 'Fuel Filter', 
        'Sparkplugs', 'Car Batteries', 'Engine Flushing', 'Gear Oil', 'Brake Fluid', 
        'Brake Parts Cleaner', 'Brake Pads', 'Brake Shoe', 'Wiperblades', 'Bulbs', 
        'ATF/CVT', 'Wheels Weights', 'Grease', 'Coolants', 'Freon'
    ]

    for i, category in enumerate(categories, start=1):
        is_Rapide = 1 if f'isRapide_{i}' in request.form else 0
        is_NonRapide = 1 if f'isNonRapide_{i}' in request.form else 0

        brand_Rapide = request.form.get(f'brandRapide_{i}', '')
        why_Rapide = request.form.get(f'whyRapide_{i}', '')
        brand_NonRapide = request.form.get(f'brandNonRapide_{i}', '')
        why_NonRapide = request.form.get(f'whyNonRapide_{i}', '')

        values.append([category, is_Rapide, brand_Rapide, why_Rapide, is_NonRapide, brand_NonRapide, why_NonRapide])

    # append
    append_to_sheet(values)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)