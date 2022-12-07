from flask import Flask, request, jsonify, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def start():
    return render_template('home.html')

@app.route('/parks', methods=['GET'])
def parks():
    return render_template('parks.html')

if __name__ == '__main__':
    app.run(debug=True)