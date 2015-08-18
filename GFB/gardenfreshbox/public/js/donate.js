//on window load:
//	If user is logged in then populate form with their data
$(window).load(function(){
	$.get('/user/me', {}, function(response){
		me = JSON.parse(response);
		var user_email = me.email;
		
		var host_site = me.host_site;
		role = me.role;
		

		$.get('/user', {'email':user_email}, function(response){
			resp = JSON.parse(response)
			$("#customer_first_name").val(resp.first_name);
			$("#customer_last_name").val(resp.last_name);
			$("#customer_email").val(resp.email);
			$("#customer_phone").val(resp.phone_number);
			$("#customer_id").val(resp.id);

			document.getElementById("customer_email").disabled = true;

		});
	});
});

//toggleReciept - Change boolean value when user turns on/off donation reciept option
function toggleReceipt(){
	var caller = document.getElementById("donation_receipt");
	if (caller.value == "on"){
		caller.value = "off";
	} else {
		caller.value = "on";
	}
}

	
//confirmDonate - check if inputs are valid, if they are then add the donation to backend
function confirmDonate() {
	if (create_new_donation_input_is_valid()){
		var today = getCurrentDate();
		$.ajax({
			type: 'put',
			url: '/sales/cashsales',
			data: {
				orderID : "",
				dateToDistribute : "",	
				lastName : $("#customer_last_name").val(),
				email : $("#customer_email").val(),
				smallBoxQuantity : "",
				phoneNumber : $("#customer_phone").val(),
				hostSiteOrderID : "-99",
				dateCreated : today,
				donations : $("#donation").val(),
				hostSitePickupID : "",
				totalPaid : "",
				shouldSendNotifications : "off",
				donationReceipt : $("#donation_receipt").val(),
				firstName : $("#customer_first_name").val(),
				largeBoxQuantity : "",
				customerID : $("#customer_id").val()
			},
			complete: function(response) {
				if (response.success == "false"){
					alert(response.message);
				} else {
					alert("Your donation was placed successfully.\nThank you.");
					location.reload();
				}
			}
		});
	}
}