from flask import Flask, render_template, jsonify
from algo import *
from searchtweets import load_credentials, gen_rule_payload, collect_results

app = Flask(__name__)

# credentials = load_credentials(filename="./app.py",
#                 yaml_key="app",
#                 env_overwrite=False)

# @app.route('/', methods=['GET'])
# def index():
#     rule = gen_rule_payload("keyword", results_per_call=100)
#     tweets = collect_results(rule, max_results=100, result_stream_args=credentials)
#     return jsonify(tweets), render_template('app.html')



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)