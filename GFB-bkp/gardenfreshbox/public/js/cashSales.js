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
	
	addHostSitesToList("#hostsitepickup_idFK",)
	
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

		
	var today = getCurrentDate();

	$("#submit").click(addCashSale);
	$("#creation_date").val(today)
});

function loadSales(){
	if($("#hostsitecreated_idFK").val() == "--Select--"){
		$("#allOrders").html("Select A Host Site");
	} else {
		$.get('/sales/cashsales', {'hostSiteName':$("#hostsitecreated_idFK").val()}, function(response){
			$("#allOrders").html(response);
			//addRowHandlers();
		});
	}
}

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
		
function addCashSale(){
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
			largeBoxQuantity : $("#large_quantity").val()
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