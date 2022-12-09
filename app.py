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
    output = {}
    output["timezones"] = ["-11", "-10", "-9", "-8", "-7", "-5", "-4", "-3", "-2", "-1", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11" ]
    output["climates"] = ["Alpine", "Desert", "Humid continental", "Ice cap", "Mediterranean", "Oceanic", "Polar", "Semi arid", "Subarctic", "Tropical monsoon", "Tropical rainforest", "Tropical savanna", "Tundra"]
    output["precipitation"] = ["Drizzle", "Hail", "Ice Crystals", "Ice Pellets", "Rain", "Small Hail", "Snow", "Snow Grains"]
    output["terrain"] = ["Alpine Tundra", "Canyon", "Desert", "Dunes", "Forest", "Hill", "Marsh", "Mountainous", "Plateau", "Valley" ]
    output["campsites"] = ["0","1"]
    output["difficulty"] = ["1","2","3","4"]
    return output


@app.route('/grades',methods=['PUT'])
def getfilter():
    filters = request.get_json()
    environment = 'w_birds' in filters or 'w_reptiles' in filters or 'w_fish' in filters or 'w_mammals' in filters or 'w_trees' in filters or 'w_flora' in filters
    trail = 't_name' in filters or 't_terrain' in filters or 't_campsites' in filters or 't_difficulty' in filters
    if environment and trail:
        query = ("SELECT DISTINCT p_parkkey FROM park LEFT JOIN state ON park.p_statekey = state.s_statekey LEFT JOIN environment ON environment.e_parkkey = park.p_parkkey LEFT JOIN trail ON trail.t_parkkey = park.p_parkkey LEFT JOIN wildlife ON wildlife.w_environmentkey = environment.e_environmentkey WHERE ")
    elif trail and not environment:
        query = ("SELECT DISTINCT p_parkkey FROM park LEFT JOIN state ON park.p_statekey = state.s_statekey LEFT JOIN trail ON trail.t_parkkey = park.p_parkkey WHERE")
    elif environment:
        query = ("SELECT DISTINCT p_parkkey FROM park LEFT JOIN state ON park.p_statekey = state.s_statekey LEFT JOIN environment ON environment.e_parkkey = park.p_parkkey LEFT JOIN wildlife ON wildlife.w_environmentkey = environment.e_environmentkey WHERE ")
    else:
        query = ("SELECT DISTINCT p_parkkey FROM park LEFT JOIN state ON park.p_statekey = state.s_statekey WHERE")
    for filter in filters:
        if filter == "t_campsites" or filter== "s_timezone":
            query = query + filter + " = " + filters[filter] + " AND "
        else:
            query = query + ' UPPER(' + filter + ") LIKE UPPER(\'%" + filters[filter] + "%\') AND "
    cursor = cnx.cursor(buffered=True)
    query = query[0:-4]
    print(query)
    cursor.execute(query)
    print("executed search")
    cursor2 = cnx.cursor()
    parks = []
    output = {}
    for result in cursor:
        parks.append(result)
    for result in parks:
        query2 = ("SELECT DISTINCT p_name, s_name, p_temperature, p_precipitation, p_location FROM park LEFT JOIN state ON state.s_statekey = park.p_statekey WHERE p_parkkey = " + str(result[0]))
        print(query2)
        cursor2.execute(query2)
        for thing in cursor2:
            output[thing[0]] = thing
    print(output)
    return output
    
if __name__ == '__main__':
    app.run(debug=True)