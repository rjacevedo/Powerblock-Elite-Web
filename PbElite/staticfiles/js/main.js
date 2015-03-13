google.load('visualization', '1.1', { packages: ['line'] });

function drawChart(circuit_num, circuit_name) {
    var width = document.getElementById('main').offsetWidth * 0.9;
    var height = document.getElementById('main').offsetHeight * 0.75;

    var chartData = new google.visualization.DataTable();
    chartData.addColumn('date', 'Time');
    chartData.addColumn('number', 'Energy Usage');
    
    var options = {
        legend: {
            position: "none"
        },
        chart: {
            title: 'Energy Usage of ' + circuit_name,
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
    
    $.ajax({
        type: "POST",
        url: "/api/getCircuitData/",
        data: {
            circuit_num: circuit_num,
        },
        success: function (data) {
            var contents = [];
            data.readings.forEach(function(v) {
                var tempDate = new Date(v.timestamp);
                contents.push([tempDate, v.reading]);
            });
            chartData.addRows(contents);

            var chart = new google.charts.Line(document.getElementById('linechart_material'));
            chart.draw(chartData, options);
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            console.log("error: " + errorThrown);
        }
    });
}

function doGet() {
    var app = UiApp.createApplication();
    var panel = app.createVerticalPanel();
    panel.add(app.createButton("button 1"));
    panel.add(app.createButton("button 2"));
    app.add(panel);
    return app;
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