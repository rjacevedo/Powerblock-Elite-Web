function updateUserDetails() {
    var email = $("#email").val();
    var firstName = $('#firstName').val();
    var lastName = $('#lastName').val();
    var address = $('#address').val();
    var city = $('#city').val();
    var country = $('#country').val();
    var postalCode = $('#postalCode').val();

    var userID = 1;
    $.ajax({
        type: "POST",
        url: "/api/updateUserData/",
        data: {
            userID: userID,
            email: email,
            firstName: firstName,
            lastName: lastName,
            address: address,
            city: city,
            country: country,
            postalCode: postalCode
        },
        success: function (data) {

        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            console.log("error: " + errorThrown);
        }
    });
}