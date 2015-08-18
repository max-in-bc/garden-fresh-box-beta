//on page load:
//	Get all customers and add them to the list with row/sort handlers to load the data to editing form
//	Add appropriate host site info to the associated host site dropdown
//	Add pickup dates to dropdown
$(window).load(function(){
	$(".interior").hide();
	
	$.get('/sales/customers', {}, function(response) {
		$("#customerList").html(response);
		addRowHandlers("custTable", null, load_user_orders);
		setupFilter();
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
	
	//Either pay in person or with paypal right now
	$("#payment_area").click(function(loc) {
		if (loc.toElement.value != null){
			var payment = loc.toElement.value
			if (payment == "Pay online"){
				$("#paypal_button").show();
				$("#submit").hide();
			}
			else if (payment == "Pay in person"){
				$("#paypal_button").hide();
				$("#submit").show();
			}
		}
	});
});

//load_order - user selected a customer so load the customers details to the form for editing
function load_order(order_id){

	$.get('/sales/cashsales', {"hostSiteName": "", "orderID":order_id}, function(response){
		resp = JSON.parse(response)
		
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
		$('html, body').animate({scrollTop:$('#editOrderScrollPosition').position().top}, 'slow');
	}	

	});
	
}

//load_user_orders - load the sales of the selected user
function load_user_orders(customer_id){
	
	document.getElementById("newAccount").style.display = "none";
	document.getElementById("subheader").style.display = "block";
	$.get('/sales/usersales',  {'email': customer_id, 'sortid':"Pickup Date"}, function(response){
		$("#allOrders").html(response);
		addRowHandlers("ordersTable", null, load_order);
		setupFilter();
	});
	var temp = document.getElementById(customer_id);
	var $this = $(temp);
	
	$this.addClass('active');
	$("#customerList").removeClass("active");
	$this.siblings().removeClass("active");
	$this.addClass("active");
	
	$.get('/user', {'email':customer_id}, function(response){

		var me = JSON.parse(response);
		$("#customerID").val(me.id);
		
	});
	
	$('html, body').animate({scrollTop:$('#userOrdersScrollPosition').position().top}, 'slow');
	
}

//placeOrder - check if inputs are valid, if they are then edit the selected order of the selected customer in th backend
function placeOrder(){
	if (create_new_order_input_is_valid()){
		var paid = 0;
		if (document.getElementById("is_paid").checked){
			paid = 1;
		}
		
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
				totalPaid : paid,
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
					location.reload();
				}
			}
		});
	}
}

//deleteClicked - if admin selected a sale to delete, then confirm it, and delete from backend
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