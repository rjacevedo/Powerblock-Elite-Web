$(document).ready(function () {
    var height = $('mainDiv').offsetHeight * 0.95;
    var calendar = $('#calendar');
    calendar.fullCalendar({
        dayClick: function (date, jsEvent, view) {
            document.getElementById('eventDate').value = date.format();
            $('#addEventModal').modal('show');
        },
        eventClick: function (calEvent, jsEvent, view) {
            $('#editEventTitle').val(calEvent.title);

            var startDate = new Date(calEvent.start);
            var startHour = startDate.getHours();
            if (startHour > 11) {
                $('#editEventStartPeriod').val('pm');
                startHour -= 12;
            }
            $('#editEventStartHour').val(startHour);
            $('#editEventStartMin').val(startDate.getMinutes());

            var endDate = new Date(calEvent.end);
            var endHour = endDate.getHours();
            if (endHour > 11) {
                $('#editEventEndPeriod').val('pm');
                endHour -= 12;
            }
            $('#editEventEndHour').val(endHour);
            $('#editEventEndMin').val(endDate.getMinutes());

            $('#editEventRoomSelect').val(calEvent.roomNum);
            $('#editEventState').val(calEvent.state);

            $('#editDeleteButton').one("click", function () {
                $.ajax({
                    type: "POST",
                    url: "/api/deleteSchedule",
                    data: { scheduleID: calEvent.id },
                    success: function (data) {
                        calendar.fullCalendar('removeEvents', calEvent.id);    
                    }
                });
            });

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
            var start = new Date(v.start);
            var end = new Date(v.end);
            addCalendarEvent(v.id, v.description, start, end, v.circuit, v.state);
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

    var startDateDefault = new Date(parseInt(dateArray[0]), parseInt(dateArray[1]) - 1, parseInt(dateArray[2]), parseInt(startHour), parseInt(startMin), 0, 0);
    startDate = startDateDefault.toUTCString();
    var endDateDefault = new Date(parseInt(dateArray[0]), parseInt(dateArray[1]) - 1, parseInt(dateArray[2]), parseInt(endHour), parseInt(endMin), 0, 0);
    endDate = endDateDefault.toUTCString();
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
            $('#eventTitle').css("border-color", "rgb(204, 204, 204)");
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
                addCalendarEvent(data, title, startDateDefault, endDateDefault, roomNum);
            }
        });
    }
}

function addCalendarEvent(id, title, start, end, roomNum, state) {
    var event = {
        id: id,
        title: title,
        roomNum: roomNum,
        start: start,
        end: end,
        state: state
    }

    var calendar = $('#calendar');
    calendar.fullCalendar('renderEvent', event);
}

function deleteCalendarEvent(eventId) {
    
}

function resetModal() {
    $('#eventTitle').attr("placeholder", "");
    $('#eventTitle').css("border-color", "initial");
    $('#modalDateError').hide();
}

function modalGetRoomSelect() {
    //hard code for now until authentication is complete
    var login = 1;
    $.getJSON("/circuits/" + login + "/", function (circuits) {
        var contents = '';
        for (i in circuits) {
            contents += '<option value="' + circuits[i].num + '">';
            contents += circuits[i].name + '</option>';
        }
        document.getElementById('eventRoomSelect').innerHTML = contents;
        document.getElementById('editEventRoomSelect').innerHTML = contents;
    });
}

function viewScheduledEvent() {
    
}