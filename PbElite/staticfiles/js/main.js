google.load('visualization', '1.1', { packages: ['line'] });

function drawChart() {
    var width = document.getElementById('main').offsetWidth * 0.9;
    var height = document.getElementById('main').offsetHeight * 0.75;

    var chartData = new google.visualization.DataTable();
    chartData.addColumn('number', 'Day');
    chartData.addColumn('number', 'Energy Usage');
    $.ajax({
        type: "POST",
        url: "/api/getCircuitData/",
        data: {
            circuit_num: 1,
        },
        success: function (data) {
            var contents = [];
            data.readings.forEach(function(v) {
                console.log(new Date(v.timestamp));
                contents.push([v.timestamp, v.reading]);
            });
            chartData.addRows(contents);
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            console.log("error: " + errorThrown);
        }
    });

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

    chart.draw(chartData, options);
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