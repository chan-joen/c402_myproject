from flask import Flask
import test

app = Flask(__name__)

comparison_str = test.comparison.to_string()

@app.route('/')
def hello_pybo():
    #return 'Hello, Pybo! local'
    return comparison_str