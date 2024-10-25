from flask import Flask, redirect, request, jsonify, render_template,send_from_directory, url_for
import pandas as pd


app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

if __name__ == '__main__':
 


    app.run(debug = True)