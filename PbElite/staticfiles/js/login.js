$(window).bind('keypress', function (e) {
    // enter is pressed
    if (e.keyCode == 13) {
        loginRequest();
    }
});

if (getCookie("username")) {
    window.location = "/home/";
}

function loginRequest() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    if (document.getElementById('stayLoggedIn').checked) {
        document.cookie = "username=" + username;
    } else {
        document.cookie = "username=; expires=Thu, 01 Jan 1970 00:00:00 UTC";
    }

    // remember to eventually encrypt the password before sending
    var postData = {
        username: username,
        password: password
    };

    makeLoginRequest(postData);
}

function makeLoginRequest(postData) {
    $.ajax({
        type: "POST",
        url: "/loginRequest/",
        data: postData,
        success: function (data) {
            if (data.loginSuccess == 1) {
                if (document.getElementById('stayLoggedIn').checked) {
                    document.cookie = 'loginsession=' + data.hash;
                }
                window.location = "/home/";
            }
        },
        error: function () {
            document.getElementById('loginError').style.display = "block";
        }
    });
}

function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for (i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') c = c.substring(1);
        if (c.indexOf(name) == 0) return c.substring(name.length, c.length);
    }
    return "";
}