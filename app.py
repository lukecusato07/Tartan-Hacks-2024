from flask import Flask, render_template, request, redirect, url_for
from algo import *

app = Flask(__name__, template_folder='./frontend/templates', static_folder='./frontend/static')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/app')
def show_form():
    return render_template('form.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    stock_name, stock_ticker = request.form['datalist_stocks'].split("-")
    stock_name, stock_ticker = stock_name.strip(), stock_ticker.strip()
    
    exchange_name = request.form['selector_exchange'].split("/")[0].upper()

    result = analyze(stock_name, 'news')

    return redirect(url_for('show_data', stock_analysis=result, stock_name=stock_name, stock_ticker=stock_ticker, exchange_name=exchange_name))

@app.route('/app/query', methods=['GET'])
def show_data():
    stock_analysis = float(request.args.get('stock_analysis'))
    decimal_points = str(stock_analysis)[::-1].find('.')
    stock_analysis_rounded = round(stock_analysis, min(decimal_points, 5))

    stock_name = request.args.get('stock_name')
    stock_ticker = request.args.get('stock_ticker')
    exchange_name = request.args.get('exchange_name')
    return render_template('show_data.html', stock_analysis=stock_analysis_rounded, stock_name=stock_name, stock_ticker=stock_ticker, exchange_name=exchange_name)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)