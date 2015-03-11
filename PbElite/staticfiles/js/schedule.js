$(document).ready(function () {
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

    console.log(date + ", " + startHour + ":" + startMin);
    var startDate = new Date(date + ", " + startHour + ":" + startMin);
    console.log(startDate);
    var startDateEpoch = startDate.getTime() / 1000;
    console.log(startDateEpoch);
    var endDate = new Date(date + ", " + endHour + ":" + endMin);
    var endDateEpoch = endDate.getTime()/1000;
    
    if (startDateEpoch > endDateEpoch) {
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

    if (startDateEpoch <= endDateEpoch && title.length > 0) {
        $("#addEventModal").modal('hide');

        //send a request to the server to store the event
        var event = {
            desc: title,
            circuit_id: roomNum,
            start_time: startDateEpoch,
            end_time: endDateEpoch,
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