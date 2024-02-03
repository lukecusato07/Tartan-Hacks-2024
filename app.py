from flask import Flask, render_template, request, redirect, url_for, jsonify
from algo import *

app = Flask(__name__, template_folder='./frontend/templates', static_folder='./frontend/static')

# credentials = load_credentials(filename="./app.py",
#                                                             yaml_key="app",
#                                                             env_overwrite=False)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/app')
def show_form():
    return render_template('form.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    print(request.form['datalist_stocks'])
    return render_template('index.html')

@app.route('/app/query')
def show_data():
    data = request.args.get('data')
    return render_template('show_data.html', data=data)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)