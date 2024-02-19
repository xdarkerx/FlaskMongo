from flask import Flask, render_template, request, jsonify, make_response
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

if __name__ == '__main__':
    app.run()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')