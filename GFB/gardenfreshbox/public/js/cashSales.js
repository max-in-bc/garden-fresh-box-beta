//On window load populate all of the dropdown menus with proper host sites and pickup dates
//	*If host site coordinator then set the host-site to the correct one in dropdown, populate the sales for that site, and lock the dropdown from being changed
$(window).load(function(){
	
	var host_site, host_site_name;
	$.get('/user/me', {}, function(response){

		if(response!=''){
			var me = JSON.parse(response);
			if (me.host_site != '' && me.role == 3){
				host_site = me.host_site;
			}
		}
	});
	$.get('/hsJSON', {}, function(response){
		var resp = JSON.parse(response);
		$("#hostsitepickup_idFK").append("<option id=NULL>--Select--</option>")
		$("#hostsitecreated_idFK").append("<option id=NULL>--Select--</option>")
		$.each(resp, function(i, item) {
			$("#hostsitepickup_idFK").append("<option id=" + item.id + ">" + item.name + "</option>")
			$("#hostsitecreated_idFK").append("<option id=" + item.id + ">" + item.name + "</option>")
			if (item.id == host_site){
				host_site_name = item.name;
				$("#hostsitecreated_idFK").val(host_site_name);
				loadSales();
			    document.getElementById("hostsitecreated_idFK").disabled=true;
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

	$("#submit").click(addCashSale);
	$("#creation_date").val(today)
});

//loadSales - if a host site is selected by admin, load the sales for that site only to the table
function loadSales(){
	if($("#hostsitecreated_idFK").val() == "--Select--"){
		$("#allOrders").html("Select A Host Site");
	} else {
		$.get('/sales/cashsales', {'hostSiteName':$("#hostsitecreated_idFK").val(), 'orderID': ""}, function(response){
			$("#allOrders").html(response);
			//addRowHandlers();
		});
	}
}

//toggleReciept - Change boolean value when user turns on/off donation reciept option
function toggleReceipt(){
	var caller = document.getElementById("donation_receipt");
	if (caller.value == "on"){
		caller.value = "off";
	} else {
		caller.value = "on";
	}
}

//toggleReciept - Change boolean value when user turns on/off email notifications option
function toggleEmail(){
	var caller = document.getElementById("email_notifications");
	if (caller.value == "on"){
		caller.value = "off";
	} else {
		caller.value = "on";
	}
}
		
//addCashSale - check inputs, if valid then add new cash sale to database and reload page
function addCashSale(){
	if (create_new_order_input_is_valid()){
		var options = document.getElementsByTagName("option");
		var distID;
		var createID;
		for (i = 0; i < options.length; i++) {
			if(options[i].value == $("#hostsitepickup_idFK").val()){
				distID = options[i].id;
				// alert("distID");
			}
			if(options[i].value == $("#hostsitecreated_idFK").val()){
				createID = options[i].id;
				// alert("createID");
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
				hostSiteOrderID : distID,
				dateCreated : $("#creation_date").val(),
				donations : $("#donation").val(),
				hostSitePickupID : createID,
				totalPaid : $("#total_paid").val(),
				shouldSendNotifications : $("#email_notifications").val(),
				donationReceipt : $("#donation_receipt").val(),
				firstName : $("#customer_first_name").val(),
				largeBoxQuantity : $("#large_quantity").val(),
				customerID : ""
			},
			complete: function(response) {
				if (response.success == "false"){
					alert(response.message);
				} else {
					alert("Order has been added successfully");
					location.reload();
				}
			}
		});
	}
}