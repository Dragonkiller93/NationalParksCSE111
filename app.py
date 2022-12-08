from flask import Flask, request, jsonify, render_template, redirect, url_for
import mysql.connector


app = Flask(__name__)

cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='nps')

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


@app.route('/grades',methods=['PUT'])
def getfilter():
    filters = request.get_json()
    query = ("SELECT p_name FROM park LEFT JOIN state ON park.p_statekey = state.s_statekey LEFT JOIN environment ON environment.e_parkkey = park.p_parkkey LEFT JOIN trail ON trail.t_parkkey = park.p_parkkey LEFT JOIN visitorcenter ON visitorcenter.vc_parkkey = park.p_parkkey LEFT JOIN wildlife ON wildlife.w_environmentkey = environment.e_environmentkey WHERE ")
    for filter in filters:
        query = query + filter + "= \"" + filters[filter] + "\" AND "
    cursor = cnx.cursor(buffered=True)
    query = query[0:-4]
    print(query)
    cursor.execute(query)
    for result in cursor:
        print(result)
    return "completed"

if __name__ == '__main__':
    app.run(debug=True)