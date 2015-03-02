google.load('visualization', '1.1', { packages: ['line'] });

function drawChart() {
    var width = document.getElementById('main').offsetWidth * 0.9;
    var height = document.getElementById('main').offsetHeight * 0.75;

    var data = new google.visualization.DataTable();
    data.addColumn('number', 'Day');
    data.addColumn('number', 'Energy Usage');

    data.addRows([
        [1, 37.8],
        [2, 30.9],
        [3, 25.4],
        [4, 11.7],
        [7, 11.9],
        [10, 8.8],
        [12, 7.6],
        [14, 12.3],
        [16, 16.9],
        [18, 12.8],
        [22, 5.3],
        [25, 6.6],
        [28, 4.8],
        [30, 4.2]
    ]);

    var options = {
        legend: {
            position: "none"
        },
        chart: {
            title: 'Energy Usage of Living Room',
        },
        series: {
            0: {axis: 'Energy'},
        },
        axes: {
            y: {
                Energy: {label: 'Power (watts)'}
            }
        },
        width: width,
        height: height,
        chartArea: {
            backgroundColor: {
                stroke: '#fff',
                strokeWidth: 3
            }
        }
    };

    var chart = new google.charts.Line(document.getElementById('linechart_material'));

    chart.draw(data, options);
}

function changeVal(circuitNum) {
    var circuit = document.getElementById('circuit' + circuitNum);
    var login = 1;
    $.ajax({
        type: "POST",
        url: "/updateCircuit/" + login + "/" + circuitNum + "/" + (circuit.value == "true" ? "0" : "1") + "/",
        success: function (data) {
            if (data['result'] == "0") {
                circuit.value = "false";
            } else {
                circuit.value = "true";
            }
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            console.log("error: " + errorThrown);
        }
    });
}

function signOut() {
    $.ajax({
        type:"GET",
        url: "/logout/",
        success: function (data) {
           document.cookie = "username=; expires=Thu, 01 Jan 1970 00:00:00 UTC";
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            console.log("error: " + errorThrown);
        }
    });
    window.location = "/login/";
}