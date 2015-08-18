$(window).load(function(){

	$.get('/hsJSON', {}, function(response){
		var resp = JSON.parse(response);
		$("#hostsitepickup_idFK").append("<option id=NULL>--Select--</option>")
		$.each(resp, function(i, item) {
			if(item.name != "Online"){
				$("#hostsitepickup_idFK").append("<option id=" + item.id + ">" + item.name + "</option>");
			}
		});
	});

	var today = getCurrentDate();

	$("#creation_date").val(today)
	$("#submit").click(placeOrder);

});

function toggleReceipt(){
	var caller = document.getElementById("donation_receipt");
	if (caller.value == "on"){
		caller.value = "off";
	} else {
		caller.value = "on";
	}
}

function toggleEmail(){
	var caller = document.getElementById("email_notifications");
	if (caller.value == "on"){
		caller.value = "off";
	} else {
		caller.value = "on";
	}
}

function placeOrder(){
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
			totalPaid : $("#total_paid").val(),
			shouldSendNotifications : $("#email_notifications").val(),
			donationReceipt : $("#donation_receipt").val(),
			firstName : $("#customer_first_name").val(),
			largeBoxQuantity : $("#large_quantity").val()
		},
		complete: function(response) {
			if (response.success == "false"){
				alert(response.message);
			} else {
				location.reload();
			}
		}
	});
}