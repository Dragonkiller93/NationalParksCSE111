// Get the element with id="defaultOpen" and click on it
let request = new XMLHttpRequest();
request.open("GET","/getdata");
request.send();
request.onload= () =>{
    data = JSON.parse(request.response);
    loadtimezones(data);
    loadclimates(data);
    loadprecipitation(data);
    loadterrain(data);
    loadcampsites(data);
    loaddifficulty(data);
}

function loadtimezones(data){
    timezonelist = document.getElementById("time-zones");
    timezones = data["timezones"]
    for (let i =0; i < Object.keys(timezones).length;i++){
        let newOption = new Option(timezones[i],timezones[i]);
        timezonelist.add(newOption,undefined);
    }
}
function loadclimates(data){
    timezonelist = document.getElementById("climate-dd");
    options = data["climates"]
    for (let i =0; i < Object.keys(options).length;i++){
        let newOption = new Option(options[i],options[i]);
        timezonelist.add(newOption,undefined);
    }
}
function loadprecipitation(data){
    timezonelist = document.getElementById("prec-dd");
    options = data["precipitation"]
    for (let i =0; i < Object.keys(options).length;i++){
        let newOption = new Option(options[i],options[i]);
        timezonelist.add(newOption,undefined);
    }
}
function loadterrain(data){
    timezonelist = document.getElementById("terrain-dd");
    options = data["terrain"]
    for (let i =0; i < Object.keys(options).length;i++){
        let newOption = new Option(options[i],options[i]);
        timezonelist.add(newOption,undefined);
    }
}
function loadcampsites(data){
    timezonelist = document.getElementById("campsite-dd");
    options = data["campsites"]
    let newOption = new Option("Yes",1);
    timezonelist.add(newOption,undefined);
    let newOption2 = new Option("No",0);
    timezonelist.add(newOption2,undefined);
}
function loaddifficulty(data){
    timezonelist = document.getElementById("diff-dd");
    options = data["difficulty"]
    for (let i =0; i < Object.keys(options).length;i++){
        let newOption = new Option(options[i],options[i]);
        timezonelist.add(newOption,undefined);
    }
}

function openCity(evt, cityName) {
    var i, tabcontent, tablinks;     // Declare all variables

    tabcontent = document.getElementsByClassName("tabcontent");    // Get all elements with class="tabcontent" and hide them
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    tablinks = document.getElementsByClassName("tablinks");     // Get all elements with class="tablinks" and remove the class "active"
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    document.getElementById(cityName).style.display = "block";     // Show the current tab, and add an "active" class to the button that opened the tab
    evt.currentTarget.className += " active";

    
}



// function applyFilter() {
//     const url = "http://127.0.0.1:5000";

//     var arr = []
//     filter1 = document.getElementById("state-name").value;
//     filter2 = document.getElementById("county-name").value;
//     filter3 = document.getElementById("time-zones").value;
//     filter4 = document.getElementById("climate-dd").value;
//     filter5 = document.getElementById("biome-type").value;
//     filter6 = document.getElementById("state-name").value;
//     filter7 = document.getElementById("county-name").value;
//     filter8 = document.getElementById("time-zones").value;
//     filter9 = document.getElementById("climate-dd").value;
//     filter10 = document.getElementById("biome-type").value;
//     filter11 = document.getElementById("state-name").value;
//     filter12 = document.getElementById("county-name").value;
//     filter13 = document.getElementById("time-zones").value;
//     filter14 = document.getElementById("climate-dd").value;
//     filter15 = document.getElementById("biome-type").value;
//     filter16 = document.getElementById("biome-type").value;
//     arr = [filter1, filter2, filter3, filter4, filter5, filter6, filter7, filter8, filter9, filter10, filter11, filter12, filter13, filter14, filter15, filter16]

//     const request = new XMLHttpRequest();
//     const method =  "GET";
//     request.open(method, url + "/parks");
//     request.send();
//     request.onload = function() {
//         data = JSON.parse(this.response);
//         var output = "";
//         for (i in data) {
//             output += "<tr>";
//             for (j in data[i]) {
//                 output += "<td>" + data[i][j] + "</td>";
//             }
//             output += "</tr>"
//         }
//         document.getElementById("showParks").innerHTML = output;
//     }
//     request.send()
// }

function applyFilter() {
    const url = "http://127.0.0.1:5000";

    filter1 = document.getElementById("state-name").value;
    filter3 = document.getElementById("time-zones").value;
    filter4 = document.getElementById("climate-dd").value;
    filter5 = document.getElementById("prec-dd").value;
    filter6 = document.getElementById("park-name").value;
    filter7 = document.getElementById("trail-name").value;
    filter8 = document.getElementById("terrain-dd").value;
    filter9 = document.getElementById("campsite-dd").value;
    filter10 = document.getElementById("diff-dd").value;
    filter11 = document.getElementById("mammal-name").value;
    filter12 = document.getElementById("reptile-name").value;
    filter13 = document.getElementById("fish-name").value;
    filter14 = document.getElementById("bird-name").value;
    filter15 = document.getElementById("tree-name").value;
    filter16 = document.getElementById("flora-name").value;

    var myDict = {};
    myDict["s_name"] = filter1;
    myDict["s_timezone"] = filter3;
    myDict["s_climate"] = filter4;
    myDict["p_precipitation"] = filter5;
    myDict["p_name"] = filter6;
    myDict["t_name"] = filter7;
    myDict["t_terrain"] = filter8;
    myDict["t_campsites"] = filter9;
    myDict["t_difficulty"] = filter10;
    myDict["w_mammals"] = filter11;
    myDict["w_reptiles"] = filter12;
    myDict["w_fish"] = filter13;
    myDict["w_birds"] = filter14;
    myDict["w_trees"] = filter15;
    myDict["w_flora"] = filter16;

    for(thing in myDict){
        if(myDict[thing]=="blank" || myDict[thing]=="")delete myDict[thing];
    }

    // const request = new XMLHttpRequest();
    // const method =  "GET";
    // 
    // request.open("GET", url + "/grades");
    // request.setRequestHeader("Content-Type", "application/json");
    // json_data = JSON.stringify(myDict);
    
    let request = new XMLHttpRequest();
    request.open("PUT","/grades",true);
    request.setRequestHeader("Content-Type", "application/json");
    request.send(JSON.stringify(myDict));
    
    request.onload= () =>{
        
        let data = JSON.parse(request.response);
        let keys = Object.keys(data);
        let text = "<table border='1' class=\"results\"><tr><th>Park Name</th><th>State</th><th>Temperature</th><th>Precipitation</th><th>Coordinates</th></tr>";
        
        for (let i = 0; i < keys.length; i++) {
            text += "<tr><td>" + keys[i] + "</td><td>" + data[keys[i]][1] + "</td><td>" + data[keys[i]][2] + "</td><td>" + data[keys[i]][3] + "</td><td>" + data[keys[i]][4] + "</td></tr>";
        }
        text += "</table>";
        document.getElementById("showParks").innerHTML = text;
    
    }
}
