from flask import Flask

myapp = Flask(__name__)

@myapp.route("/ravi")
def ravi():
        return "Hello, How are you doing"



