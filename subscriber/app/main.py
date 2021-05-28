import time
from flask import Flask
from flask import request
from db_handler import DbHandler
from flask_cors import CORS

app = Flask(__name__)
db_handler = DbHandler()
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/subscribe", methods=['POST'])
def subscribe():
    global db_handler
    print(request.headers)
    email = request.headers.get('email')
    application = request.headers.get('application')
    print(email)
    print(application)
    before = time.time()
    db_handler.subscribe(email, application)
    after = time.time()
    return f"<p>{(after-before)*1000}ms</p>"

@app.route("/unsubscribe", methods=['POST'])
def unsubscribe():
    global db_handler
    print(request.headers)
    email = request.headers.get('email')
    application = request.headers.get('application')
    print(email)
    print(application)
    before = time.time()
    db_handler.unsubscribe(email, application)
    after = time.time()
    return f"<p>{(after-before)*1000}ms</p>"

