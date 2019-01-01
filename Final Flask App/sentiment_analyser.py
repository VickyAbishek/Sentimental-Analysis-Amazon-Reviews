import os.path
from flask import Flask, Response, request
from flask_cors import CORS, cross_origin
from flask import jsonify # <- `jsonify` instead of `json`
from mymodel import getSentiment

# app = Flask(__name__)
app = Flask(__name__, static_url_path = "", static_folder = "media")

app.config['SECRET_KEY'] = 'temp_secret_key'
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/foo": {"origins": "http://localhost:port"}})

@app.route('/foo', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def foo():
    return request.json['inputVar']

def root_dir():  # pragma: no cover
    return os.path.abspath(os.path.dirname(__file__))

def get_file(filename):  # pragma: no cover
    try:
        src = os.path.join(root_dir(), filename)
        return open(src).read()
    except IOError as exc:
        return str(exc)

@app.route("/")
def index():
    return __name__

@app.route("/cunning_linguists")
def test1():
    content = get_file('home.html')
    return Response(content, mimetype="text/html")

@app.route("/demo")
def test2():
    content = get_file('demo.html')
    return Response(content, mimetype="text/html")    

@app.route('/getsentiment', methods = ['POST'])
# @cross_origin(origin='localhost')
def get_post_javascript_data():
    # jsdata = request.form['javascript_data']
    # print(jsdata)
    # response = jsonify({'some': 'data'})
    # response.headers.add('Access-Control-Allow-Origin', '*')
    received_value = request.data
    print(received_value)
    return getSentiment(received_value)
    # return "shit"

if __name__ == "__main__":
    app.run()