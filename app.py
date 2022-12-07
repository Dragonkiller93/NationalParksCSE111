from flask import Flask, request, jsonify, render_template, redirect, url_for
import mysql.connector


app = Flask(__name__)

#cnx = mysql.connector.connect(user='scott', password='password', host='127.0.0.1', database='employees')

@app.route('/')
def start():
    return render_template('home.html')

@app.route('/parks', methods=['GET'])
def parks():
    return render_template('parks.html')


@app.route('/getdata',methods=['GET'])
def gettimezones():
    timezones = {"timezones":["-1","-2","-3"]}
    return timezones

if __name__ == '__main__':
    app.run(debug=True)