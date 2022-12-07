// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();

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
    
    let request = new XMLHttpRequest();
    request.open("GET","/getdata");
    request.send();
    request.onload= () =>{
        data = JSON.parse(request.response);
        loadtimezones(data);
    }

    timezonelist = document.getElementById("time-zones");
    document.getElementById(cityName).style.display = "block";     // Show the current tab, and add an "active" class to the button that opened the tab
    evt.currentTarget.className += " active";
    }
    function loadtimezones(data){
        timezones = data["timezones"]
        for (let i =0; i < Object.keys(timezones).length;i++){
            let newOption = new Option(timezones[i],timezones[i]);
            timezonelist.add(newOption,undefined);
        }
    }