$("#registrationKey").click(clearField("registration"));

function completeRegistration() {
    if ($("#registrationKey").val() == "") {
        incompleteField("registrationKey", "Please fill in a registration key");
    } 

    if ($("#username").val() == "") {
        incompleteField("username", "Please enter a username");
    } else {
        clearField("username");
    }

    if ($("#password").val() == "") {
        incompleteField("password", "Please enter a password");
    } else {
        clearField("password");
    }

    if ($("#email").val() == "") {
        incompleteField("email", "Please enter an email");
    } else {
        clearField("email");
    }

    if ($("#address").val() == "") {
        incompleteField("address", "Please enter an address");
    } else {
        clearField("address");
    }

    if($("#city").val() == "") {
        incompleteField("city", "Please enter a city");
    } else {
        clearField("city");
    }

    if ($("#country").val() == "") {
        incompleteField("country", "Please enter a country");
    } else {
        clearField("country");
    }

    if ($("#postalCode").val() == "") {
        incompleteField("postalCode", "Please enter a postal code");
    } else {
        clearField("postalCode");
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