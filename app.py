from flask import Flask, render_template, redirect, request
from flask_cors import CORS
from controllers import urls


app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html', link='', urlsearch='')
    if request.method == 'POST':
        data = request.form
        link = urls.create(data)
    return render_template('home.html', link=link, urlsearch=data['urlsearch'])

@app.route('/<code>')
def get_url(code):
    getUrl = urls.get(code)
    if getUrl:
        return redirect(f"https://{getUrl}")
    else: 
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
