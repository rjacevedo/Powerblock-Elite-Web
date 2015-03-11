﻿$(document).ready(function () {
    var height = $('mainDiv').offsetHeight * 0.95;
    var calendar = $('#calendar');
    calendar.fullCalendar({
        dayClick: function (date, jsEvent, view) {
            document.getElementById('eventDate').value = date.format();
            $('#addEventModal').modal('show');
        },
        eventClick: function (calEvent, jsEvent, view) {
            $('#removeEventModal').modal('show');
        },
        height: height,
        header: {
            left: "prev,next, today",
            center: "title",
            right: "month,basicWeek,basicDay"
        },
        eventRender: function (event, element) {
            element.attr('title', event.description);
        }
    });

    var login = 1;
    $.getJSON("/api/getCalendarEvents/", { userID: login }, function (calendarEvents) {
        calendarEvents.forEach(function (v) {
            var start = new Date(v.start*1000);
            var end = new Date(v.end*1000);
            addCalendarEvent(v.description, start, end, v.circuit);
        });
    });
});

function addEvent() {
    var title = document.getElementById('eventTitle').value;
    var roomNum = document.getElementById('eventRoomSelect').value;
    var roomState = document.getElementById('eventRoomState').value;
    var roomName = $("#eventRoomSelect option:selected").text();
    var roomDescription = roomName + " is " + roomState;

    var date = document.getElementById('eventDate').value;
    var dateArray = date.split("-");
    var startHour = parseInt(document.getElementById('eventStartHour').value);
    var startMin = document.getElementById('eventStartMin').value;
    var startPeriod = document.getElementById('eventStartPeriod').value;
    var endHour = parseInt(document.getElementById('eventEndHour').value );
    var endMin = document.getElementById('eventEndMin').value;
    var endPeriod = document.getElementById('eventEndPeriod').value;

    if (startPeriod == 'pm') {
        startHour += 12;
    }

    if (endPeriod == 'pm') {
        endHour += 12;
    }

    var startDate = new Date(parseInt(dateArray[0]), parseInt(dateArray[1]) - 1, parseInt(dateArray[2]), parseInt(startHour), parseInt(startMin), 0, 0);
    startDate = startDate.toUTCString();
    var endDate = new Date(parseInt(dateArray[0]), parseInt(dateArray[1]) - 1, parseInt(dateArray[2]), parseInt(endHour), parseInt(endMin), 0, 0);
    endDate = endDate.toUTCString();
    
    if (startDate > endDate) {
        $('#modalDateError').show();

        $('.modalDate').off('click');
        $('.modalDate').click(function () {
            $('#modalDateError').hide();
        });
    } 
    
    if (title.length == 0) {
        $('#eventTitle').attr("placeholder", "Please enter a title");
        $('#eventTitle').css("border-color", "red");

        $('#eventTitle').off("click");
        $('#eventTitle').click(function () {
            $('#eventTitle').attr("placeholder", "");
            $('#eventTitle').css("border-color", "initial");
        });
    }

    if (startDate <= endDate && title.length > 0) {
        $("#addEventModal").modal('hide');

        //send a request to the server to store the event
        var event = {
            desc: title,
            circuit_id: roomNum,
            start_time: startDate,
            end_time: endDate,
            onoff: roomState
        }

        $.ajax({
            type: "POST",
            url: "/api/newCalenderEvent/",
            data: event,
            success: function (data) {
                addCalendarEvent(title, startDate, endDate, roomNum);
                console.log("event added");
            }
        });
    }
}

function addCalendarEvent(description, start, end, roomNum) {
    var event = {
        title: description,
        roomNum: roomNum,
        start: start,
        end: end
    }

    var calendar = $('#calendar');
    calendar.fullCalendar('renderEvent', event);
}

function resetModal() {
    $('#eventTitle').attr("placeholder", "");
    $('#eventTitle').css("border-color", "initial");
    $('#modalDateError').hide();
}