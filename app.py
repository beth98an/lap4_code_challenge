from flask import Flask, render_template, redirect
from flask_cors import CORS
from controllers import urls



app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/<code>')
def get_url(code):
    getUrl = urls.get(code)
    return redirect(f"https://{getUrl}")

