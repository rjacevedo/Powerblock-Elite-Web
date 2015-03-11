$("#registrationKey").click(clearField("registration"));

function completeRegistration() {
    var good = true;
    if ($("#registrationKey").val() == "") {
        good = false;
        incompleteField("registrationKey", "Please fill in a registration key");
    } 

    if ($("#username").val() == "") {
        good = false;
        incompleteField("username", "Please enter a username");
    } else {
        clearField("username");
    }

    if ($("#password").val() == "") {
        good = false;
        incompleteField("password", "Please enter a password");
    } else {
        clearField("password");
    }

    if ($("#email").val() == "") {
        good = false;
        incompleteField("email", "Please enter an email");
    } else {
        clearField("email");
    }

    if ($("#address").val() == "") {
        good = false;
        incompleteField("address", "Please enter an address");
    } else {
        clearField("address");
    }

    if($("#city").val() == "") {
        good = false;
        incompleteField("city", "Please enter a city");
    } else {
        clearField("city");
    }

    if ($("#country").val() == "") {
        good = false;
        incompleteField("country", "Please enter a country");
    } else {
        clearField("country");
    }

    if ($("#postalCode").val() == "") {
        good = false;
        incompleteField("postalCode", "Please enter a postal code");
    } else {
        clearField("postalCode");
    }
    if (good) {
        $.ajax({
            type: "POST",
            url: "/api/registerNewUser/",
            data: {
                registrationKey: $("#registrationKey").val(),
                username: $("#username").val(),
                password: $("#password").val(),
                firstname: 'placeholder',
                lastname: 'placeholder',
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
    $("#" + element).attr("border-color", "initial");
}