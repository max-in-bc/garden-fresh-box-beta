//on page load:
//	Check if user is logged in, if they are then load users info to form
//	Update dropdown with correct pickup dates and host sites
//	Click listener for payment area
$(window).load(function(){

	$("#paypal_submit").hide();
	$.get('/user/me', {}, function(response){
		if (response != ""){
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
		}
	});
		
	$.get('/hsJSON', {}, function(response){
		var resp = JSON.parse(response);
		$("#hostsitepickup_idFK").append("<option id=NULL>--Select--</option>")
		$.each(resp, function(i, item) {
			if(item.name != "Online"){
				$("#hostsitepickup_idFK").append("<option id=" + item.id + ">" + item.name + "</option>");
			}
		});
	});
	
	$.get('/sales/datesJSON', {}, function(response){
		var resp = JSON.parse(response);
		$("#distribution_date").append("<option value=\"--Select--\" id=NULL>--Select--</option>")
		$.each(resp, function(i, item) {
			var orderDate = new Date(Date.parse(item.pickup_date));
			orderDate.setDate(orderDate.getDate()-12);
			var todaysDate = new Date(Date.parse(getCurrentDate()));
			
			if (todaysDate <= orderDate)
				$("#distribution_date").append("<option value=\"" + item.pickup_date + "\" id=\"" + item.id + "\">" + item.pickup_date + "</option>")
			if ($("#distribution_date").val() == '--Select--')
				$("#distribution_date").val(item.pickup_date);
			
		});
	});

	var today = getCurrentDate();
	document.getElementById("creation_date").disabled = true;
	$("#creation_date").val(today);
	$("#payment_area").click(function(loc) {
		if (loc.toElement.value != null){
			var payment = loc.toElement.value
			if (payment == "Pay online"){
				$("#paypal_submit").show();
				$("#paylater_submit").hide();
			}
			else if (payment == "Pay in person"){
				$("#paypal_submit").hide();
				$("#paylater_submit").show();
			}
		}
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

//toggleEmail - Change boolean value when user turns on/off email noti option
function toggleEmail(){
	var caller = document.getElementById("email_notifications");
	if (caller.value == "on"){
		caller.value = "off";
	} else {
		caller.value = "on";
	}
}

//placeOrder - check if form is valid, if it is then place the order to the backend
function placeOrder(button){
	if (create_new_order_input_is_valid()){
		var is_paid = "0";
		if (button.id == "paypal_submit"){ 
			is_paid = "1";
		} //pay in person
		var options = document.getElementsByTagName("option");
		var distID;
		for (i = 0; i < options.length; i++) {
			if(options[i].value == $("#hostsitepickup_idFK").val()){
				distID = options[i].id;
			}
		}
		
		$.ajax({
			type: 'put',
			url: '/sales/cashsales',
			data: {
				orderID : "",
				dateToDistribute : $("#distribution_date").val(),	
				lastName : $("#customer_last_name").val(),
				email : $("#customer_email").val(),
				smallBoxQuantity : $("#small_quantity").val(),
				phoneNumber : $("#customer_phone").val(),
				hostSiteOrderID : "-99",
				dateCreated : $("#creation_date").val(),
				donations : $("#donation").val(),
				hostSitePickupID : distID,
				totalPaid : is_paid,
				shouldSendNotifications : $("#email_notifications").val(),
				donationReceipt : $("#donation_receipt").val(),
				firstName : $("#customer_first_name").val(),
				largeBoxQuantity : $("#large_quantity").val(),
				customerID : $("#customer_id").val()
			},
			complete: function(response) {
				if (response.success == "false"){
					alert(response.message);
				} else {
					if (is_paid == "0"){
						alert("Your order has been placed.");
						location.reload();
					}
				}
			}
		});
	}

}
