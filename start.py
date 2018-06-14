from flask import Flask

myapp = Flask(__name__)

@myapp.route("/soelwin")
def soelwin():
        return "Hello, How are you doing"



