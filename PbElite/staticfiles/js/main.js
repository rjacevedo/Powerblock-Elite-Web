google.load('visualization', '1.1', { packages: ['line'] });


var currentnum = -1;
var currentname = "";
function drawChart(circuit_num, circuit_name) {
    var width = document.getElementById('main').offsetWidth * 0.9;
    var height = document.getElementById('main').offsetHeight * 0.75;
    if (!circuit_num || !circuit_name) {
        circuit_num = currentnum;
        circuit_name = currentname;
    }
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
            if(data != "No Circuits"){
                data.readings.forEach(function(v) {
                    var tempDate = new Date(v.timestamp);
                    contents.push([tempDate, v.reading]);
                });
                chartData.addRows(contents);
            }

            var chart = new google.charts.Line(document.getElementById('linechart_material'));
            chart.draw(chartData, options);
            currentname = circuit_name;
            currentnum = circuit_num;
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            console.log("error: " + errorThrown);
        }
    });
}

setInterval(function(){ drawChart(); }, 3000);

function changeVal(circuitNum) {
    var circuit = document.getElementById('circuit' + circuitNum);
    var login = 1;
    $.ajax({
        type: "POST",
        url: "/updateCircuit/" + circuitNum + "/" + (circuit.value == "true" ? "0" : "1") + "/",
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

function addNewRoom() {
    var roomName = $('#modalNewRoom').val();
    $.ajax({
        type: "POST",
        url: "/api/addARoom/",
        data: { roomName: roomName },
        success: function(circuitID) {
            console.log(circuitID);
            var contents = '<tr class="spacing">';
            contents += '<td><span><input type="hidden" id="circuit' + circuitID + '" value="' + roomName + '" /></span>';
            contents += '<button type="button" class="btn btn-xs btn-danger btn-number" onclick="deleteRoom('+circuitID+')">';
            contents += '<span class="glypicon glyphicon-minus"></span>';
            contents += '</button>';
            contents += '<span id="display' + circuitID + '" style="cursor: pointer; margin-left: 3px;" onclick="drawChart(' + circuitID + ', \'' + roomName + '\')">' + roomName + '</span>';
            contents += '</td>';
            contents += '<td><div class="btn-group btn-toggle" style="padding-left:20px">';
            contents += '<button class="btn btn-primary active" onclick="changeVal(' + circuitID + ')">On</button>';
            contents += '<button class="btn btn-default" onclick="changeVal(' + circuitID + ')">Off</button>';
            contents += '</div></td>';
            contents += '</tr>';

            $('.circuitList tr:last').before(contents);
        }
    });
}

function deleteRoom(circuitID) {
    $.ajax({
        type: "POST",
        url: "/api/deleteARoom/",
        data: { circuitID: circuitID },
        success: function(data) {
            $('#circuit'+circuitID).closest('tr').remove();
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