//on page load:
//	Load list of donations to table
//	Add correct hs and pickup dates to dropdown menus for form
$(window).load(function(){
	$.get('/user/me', {}, function(response){
		if(response!=''){
			var me = JSON.parse(response);
			if (me.email != ''){
				email_str = 'email='.concat(me.email);
				$.get('/sales/userdonations', email_str, function(response){
					$("#allOrders").html(response);
					setupFilter();
				});
			}
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
		$("#distribution_date").append("<option id=NULL>--Select--</option>")
		$.each(resp, function(i, item) {
			$("#distribution_date").append("<option id=" + item.id + ">" + item.pickup_date + "</option>")
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
			largeBoxQuantity : $("#large_quantity").val(),
			customerID : $("#customer_id").val()
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

