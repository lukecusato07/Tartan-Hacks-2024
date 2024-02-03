from flask import Flask, render_template, request, redirect, url_for, json
from algo import *
from searchtweets import load_credentials, gen_rule_payload, collect_results

app = Flask(__name__, template_folder='./frontend/templates', static_folder='./frontend/static')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/app')
def show_form():
    return render_template('form.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    stock = request.form['datalist_stocks']
    exchange = request.form['selector_exchange'].split("/")[0].upper()

    result = analyze(stock, 'google')

    return redirect(url_for('show_data', stock_analysis=result, stock_name=stock, exchange_name=exchange))

@app.route('/app/query')
def show_data():
    stock_analysis = request.args.get('stock_analysis')
    stock_name = request.args.get('stock_name')
    exchange_name = request.args.get('exchange_name')
    return render_template('show_data.html', stock_analysis=stock_analysis, stock_name=stock_name, exchange_name=exchange_name)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)