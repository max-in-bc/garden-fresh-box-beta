//on page load:
//	Load list of logged in users Orders to table
//	Add correct hs and pickup dates to dropdown menus for form
//	Add paypal functionality
$(window).load(function(){
	$.get('/user/me', {}, function(response){
		if(response!=''){
			var me = JSON.parse(response);
			if (me.email != ''){
				$.get('/sales/usersales',  {'email': me.email, 'sortid':"Pickup Date"}, function(response){
					$("#allOrders").html(response);
					addRowHandlers("ordersTable", sortTable, load_order);
					setupFilter();
				});
				
				$.get('/user', {'email':me.email}, function(response2){
					var me2 = JSON.parse(response2);
					$("#customerID").val(me2.id);
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
	$("#creation_date").val(today)
	$("#submit").click(placeOrder);
	
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

//sortTable - custom sort function for order table
function sortTable(sortid){
	$.get('/user/me', {}, function(response){
		if(response!=''){
			var me = JSON.parse(response);
			if (me.email != ''){
				$.get('/sales/usersales',  {'email':me.email, 'sortid':sortid}, function(response){
					var filtertext = $("#filterbox").val()
					$("#allOrders").html(response);
					addRowHandlers("ordersTable", sortTable, load_order);
					setupFilter();
					$("#filterbox").val(filtertext);
					$("#filterbox").keyup();
				});
				
				$.get('/user', {'email':me.email}, function(response2){
					var me2 = JSON.parse(response2);
					$("#customerID").val(me2.id);
				});
			}
		}
	});
}

//toggleReciept - Change boolean value when user turns on/off email notifications option
function toggleReceipt(){
	var caller = document.getElementById("donation_receipt");
	if (caller.value == "on"){
		caller.value = "off";
	} else {
		caller.value = "on";
	}
}

//toggleEmail - Change boolean value when user turns on/off email notifications option
function toggleEmail(){
	var caller = document.getElementById("email_notifications");
	if (caller.value == "on"){
		caller.value = "off";
	} else {
		caller.value = "on";
	}
}

//placeOrder - check if inputs are valid, if they are then edit current order to backend
function placeOrder(button){
	var is_paid = "0";
	if (button.id == "paypal_submit"){ 
		is_paid = "1";
	} //pay in person
	
	if (create_new_order_input_is_valid()){
		$.ajax({
			type: 'put',
			url: '/sales/cashsales',
			data: {
				orderID : $("#orderID").val(),
				dateToDistribute : $("#distribution_date").val(),	
				lastName : $("#customer_last_name").val(),
				email : $("#customer_email").val(),
				smallBoxQuantity : $("#small_quantity").val(),
				phoneNumber : $("#customer_phone").val(),
				hostSiteOrderID : "-99",
				dateCreated : $("#creation_date").val(),
				donations : $("#donation").val(),
				hostSitePickupID : $("#siteID").val(),
				totalPaid : is_paid,
				shouldSendNotifications : $("#email_notifications").val(),
				donationReceipt : $("#donation_receipt").val(),
				firstName : $("#customer_first_name").val(),
				largeBoxQuantity : $("#large_quantity").val(),
				customerID : $("#customerID").val()
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

//user selected a row, so update that order to the form and select the row
function load_order(order_id){
	
	$.get('/sales/cashsales', {"hostSiteName": "", "orderID":order_id}, function(response){
		resp = JSON.parse(response)
		$("#allOrders").removeClass("active");
		$("#" + order_id).addClass("active");
		$("#" + order_id).siblings().removeClass("active");
		
		if (resp.total_paid > 0){
			//cannot change completed orders
			document.getElementById("newAccount").style.display = "none";
			document.getElementById("subheader").style.display = "block";

		} 
		else{
			document.getElementById("newAccount").style.display = "block";
			document.getElementById("subheader").style.display = "none";
			
			$("#customer_first_name").val(resp.customer_first_name);
			$("#customer_last_name").val(resp.customer_last_name);
			$("#customer_email").val(resp.customer_email);
			$("#customer_phone").val(resp.customer_phone);
			$("#creation_date").val(resp.creation_date);
			$("#distribution_date").val(resp.distribution_date);
			$("#small_quantity").val(resp.small_quantity);
			$("#large_quantity").val(resp.large_quantity);
	
			pid = resp.hostsitepickup_idFK;
			$.get('/hsJSON', {}, function(response){
				var resp = JSON.parse(response);
				$.each(resp, function(i, item) {
					if(item.id == pid){
						$("#hostsitepickup_idFK").val(item.name);
						$("#siteID").val(item.id);
					}
				});
			});
		
		$("#orderID").val(order_id);
		$("#siteID").val(order_id);
		$('html, body').animate({scrollTop:$('#scrollPosition').position().top}, 'slow');
	}	
		 val = resp.small_quantity * 15;
		 otherval = resp.large_quantity * 20;
		 document.forms[0].amount.value = val + otherval;
	});
}

//deleteClicked - user selected to delete a record that is still within limit date, confirm and delete
function deleteClicked(event){
	if (confirm('Are you sure you want to delete this record?')) {
		var order_id = event.target.id.split("_")[1];
		$.ajax({
			type: 'put',
			url: '/sales/cashsales',
			data: {
				orderID : order_id,
				dateToDistribute : "",	
				lastName : "",	
				email : "",	
				smallBoxQuantity :"",	
				phoneNumber : "",	
				hostSiteOrderID : "-99",
				dateCreated :"",	
				donations : "",	
				hostSitePickupID :"",	
				totalPaid : "",	
				shouldSendNotifications : "",	
				donationReceipt :"",	
				firstName :"",	
				largeBoxQuantity :"",	
				customerID : "",	
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
}