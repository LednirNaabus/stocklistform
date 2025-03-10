from flask import Flask, render_template, request, redirect
from google_sheets import append_to_sheet
from config.config import CATEGORIES

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/submit", methods=['POST'])
def submit():
    values = []

    for i, category in enumerate(CATEGORIES, start=1):
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