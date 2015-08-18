
$(window).load(function(){
	$("#confirmDonate").click(confirmDonate);
});


function toggleReceipt(){
	var caller = document.getElementById("donation_receipt");
	if (caller.value == "on"){
		caller.value = "off";
	} else {
		caller.value = "on";
	}
}

		
function confirmDonate() {
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
			phoneNumber : $("#phone").val(),
			hostSiteOrderID : "-99",
			dateCreated : today,
			donations : $("#donation").val(),
			hostSitePickupID : "",
			totalPaid : $("#donation").val(),
			shouldSendNotifications : "off",
			donationReceipt : $("#donation_receipt").val(),
			firstName : $("#customer_first_name").val(),
			largeBoxQuantity : ""
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