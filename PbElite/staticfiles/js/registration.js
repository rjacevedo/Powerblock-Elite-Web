$(document).ready(function() {
    $("#registrationKey").focus(function() {
        clearField("registrationKey");
        console.log("registratoin key selected");
    });

    $("#username").focus(function() {
        clearField("username");
    });

    $("#password").focus(function() {
        clearField("password");
    });

    $("#email").focus(function() {
        clearField("email");
    });

    $("#address").focus(function() {
        clearField("address");
    });

    $("#city").focus(function() {
        clearField('city');
    });

    $('#country').focus(function() {
        clearField('country');
    });

    $('#postalCode').focus(function() {
        clearField('postalCode');
    });
});

function completeRegistration() {
    var good = true;
    if ($("#registrationKey").val() == "") {
        good = false;
        incompleteField("registrationKey", "Please fill in a registration key");
    } 

    if ($("#username").val() == "") {
        good = false;
        incompleteField("username", "Please enter a username");
    } 

    if ($("#password").val() == "") {
        good = false;
        incompleteField("password", "Please enter a password");
    } 

    if ($("#email").val() == "") {
        good = false;
        incompleteField("email", "Please enter an email");
    } 

    if($('#firstName').val() == "") {
        good = false;
        incompleteField("firstName", "Please enter your first name");
    }

    if($('#lastname').val() == "") {
        good = false;
        incompleteField("lastName", "Please enter your last name");
    }

    if ($("#address").val() == "") {
        good = false;
        incompleteField("address", "Please enter an address");
    }

    if($("#city").val() == "") {
        good = false;
        incompleteField("city", "Please enter a city");
    }

    if ($("#country").val() == "") {
        good = false;
        incompleteField("country", "Please enter a country");
    } 

    if ($("#postalCode").val() == "") {
        good = false;
        incompleteField("postalCode", "Please enter a postal code");
    }

    if (good) {
        $.ajax({
            type: "POST",
            url: "/api/registerNewUser/",
            data: {
                registrationKey: $("#registrationKey").val(),
                username: $("#username").val(),
                password: $("#password").val(),
                firstname: $('#firstName').val(),
                lastname: $('#lastName').val(),
                address: $("#address").val(),
                email: $("#email").val(),
                city: $("#city").val(),
                country: $("#country").val(),
                postalCode: $("#postalCode").val(),
            },
            success: function (data) {           
                console.log(data);
            }
        });
    }
    

}

function incompleteField(element, placeholder) {
    $("#" + element).attr("placeholder", placeholder);
    $("#" + element).css("border-color", "red");
}

function clearField(element) {
    $("#" + element).attr("placeholder", "");
    $("#" + element).css("border-color", "rgb(204, 204, 204)");
}