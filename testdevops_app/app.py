from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
	return jsonify(msg="Test Devops Dan Hormachea")

