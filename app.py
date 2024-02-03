from flask import Flask, render_template, request, redirect, url_for, json
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
    exchange_name = request.form['selector_exchange'].split("/")[0].upper()

    result = analyze(stock_ticker, 'news')
    urls = scrape_news(stock_ticker)
    print(urls)

    return redirect(url_for('show_data', stock_analysis=result, stock_name=stock_name, stock_ticker=stock_ticker, exchange_name=exchange_name))

@app.route('/app/query')
def show_data():
    stock_analysis = request.args.get('stock_analysis')
    stock_name = request.args.get('stock_name')
    stock_ticker = request.args.get('stock_ticker')
    exchange_name = request.args.get('exchange_name')
    return render_template('show_data.html', stock_analysis=stock_analysis, stock_name=stock_name, stock_ticker=stock_ticker, exchange_name=exchange_name)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)