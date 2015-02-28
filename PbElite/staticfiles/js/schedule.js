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
        },
        /*eventMouseover: function (event, jsEvent, view) {
            console.log('in here');
            $('.fc-event-inner', this).append('<div class="hover-end">' + "abc" + '</div>');
        },

        eventMouseout: function (event, jsEvent, view) {
           // $('#' + event.id).remove();
        }*/
    });

    var startDate = new Date("February 2, 2015 08:00:00");
    var endDate = new Date("February 2, 2015 15:00:00");

    for (var i = 0; i < 4; i++) {
        for (var j = 0; j < 5; j++) {
            addCalendarEvent("Attending Lectures", startDate, endDate);

            startDate.setDate(startDate.getDate() + 1);
            endDate.setDate(endDate.getDate() + 1);
        }
        startDate.setDate(startDate.getDate() + 2);
        endDate.setDate(endDate.getDate() + 2);
    }
});

function addEvent() {
    var title = document.getElementById('eventTitle').value;
    var room = document.getElementById('eventRoomSelect').value;
    var roomState = document.getElementById('eventRoomState').value;
    var roomDescription = room + " is " + roomState;

    var date = document.getElementById('eventDate').value;
    var startHour = document.getElementById('eventStartHour').value;
    var startMin = document.getElementById('eventStartMin').value;
    var startPeriod = document.getElementById('eventStartPeriod').value;
    var endHour = document.getElementById('eventEndHour').value;
    var endMin = document.getElementById('eventEndMin').value;
    var endPeriod = document.getElementById('eventEndPeriod').value;

    if(startPeriod == 'pm') {
        startHour += 12;
    }

    var startDate = new Date(date + ", " + startHour + ":" + startMin);
    var endDate = new Date(date + ", " + endHour + ":" + endMin);

    addCalendarEvent(title, startDate, endDate, roomDescription);
}

function addCalendarEvent(title, start, end, room) {
    console.log(room);
    var event = {
        title: title,
        description: room,
        start: start,
        end: end
    }

    var calendar = $('#calendar');
    calendar.fullCalendar('renderEvent', event);
}