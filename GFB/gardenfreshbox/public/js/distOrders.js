//on window load:
//	Check if admin or host site coordinator, then check if there is a site associated with the user:
//		If host site associated and user is an admin then remove the associated site, this was used to load the correct site when this page was opened from the order list
//	Populate dropdowns with host sites and pickup dates
$(window).load(function(){
	var host_site, host_site_name;
	
	$(".interior").hide();
	$.get('/user/me', {}, function(response){
	
		if(response!=''){
			var me = JSON.parse(response);
			if (me.host_site != '' && (me.role == 3 || me.role == 2)){
				
				host_site = me.host_site;
				if (me.role == 2){
					$.ajax({
						type: 'put',
						url: '/user/me',
						data: {
							siteID :  "",
							changed: "false"
						},
						complete: function(response) {
							if (response.success == "false"){
								alert(response.message);
							}
						}
					});
					
				}
			}
		}
	});
	
	$.get('/hsJSON', {}, function(response){
		var resp = JSON.parse(response);
		$("#hsDropDown").append("<option id=NULL>--Select--</option>");
		$("#hostsitepickup_idFK").append("<option id=NULL>--Select--</option>");
		$.each(resp, function(i, item) {
			if(item.name != "Online"){
				$("#hsDropDown").append("<option id=" + item.id + ">" + item.name + "</option>");
				$("#hostsitepickup_idFK").append("<option id=" + item.id + ">" + item.name + "</option>");
				if (item.id == host_site){
					host_site_name = item.name;
					$("#hsDropDown").val(host_site_name);
					$("#hostsitepickup_idFK").val(host_site_name);
					loadSales();
				}
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
			
			$("#distribution_date").append("<option value=\"" + item.pickup_date + "\" id=\"" + item.id + "\">" + item.pickup_date + "</option>")
			
		});
	});

	var today = getCurrentDate();

	$("#submit").click(addCashSale);
	$("#creation_date").val(today)
});

function openMenu(){
	$(".interior").show();
	$("#neworder").hide();
	$("#customer_first_name").val("");
	$("#customer_last_name").val("");
	$("#customer_email").val("");
	$("#customer_phone").val("");
	$("#hostsitepickup_idFK").val("--Select--");
	$("#distribution_date").val("--Select--");
	$("#small_quantity").val("");
	$("#large_quantity").val("");
	$("#creation_date").val(getCurrentDate());
	

	$("#customerID").val("");
	$("#orderID").val("");
	$("#siteID").val("");
	
	
}

function loadSales(){
	if ($("#hsDropDown").val() == "--Select--"){
		$("#list").html("Select A Host Site");
	} else {
		$.get('/sales/dist', {'hostSiteName':$("#hsDropDown").val(), 'sortid':"Email"}, function(response){
			$("#list").html(response);
			addRowHandlers("usersTable", sortTable, load_order);
			setupFilter();
		});
	}
}

function sortTable(sortid){
	if ($("#hsDropDown").val() == "--Select--"){
		$("#list").html("Select A Host Site");
	} else {
		$.get('/sales/dist', {'hostSiteName':$("#hsDropDown").val(), 'sortid':sortid}, function(response){
			var filtertext = $("#filterbox").val()
			$("#list").html(response);
			addRowHandlers("usersTable", sortTable, load_order);
			setupFilter();
			$("#filterbox").val(filtertext);
			$("#filterbox").keyup();
		});
	}
}

function load_order(order_id){
	$.get('/sales/cashsales', {"hostSiteName": "", "orderID":order_id}, function(response){
		resp = JSON.parse(response)
		
		$("#list").removeClass("active");
		$("#" + order_id).addClass("active");
		$("#" + order_id).siblings().removeClass("active");
		
		
		if (resp.total_paid > 0){
			$(".interior").hide();
			$("#neworder").show();
		}else{
			openMenu();
			$("#neworder").show();
			
			
			$("#customer_first_name").val(resp.customer_first_name);
			$("#customer_last_name").val(resp.customer_last_name);
			$("#customer_email").val(resp.customer_email);
			$("#customer_phone").val(resp.customer_phone);
			$("#creation_date").val(resp.creation_date);
			$("#distribution_date").val(resp.distribution_date);
			$("#small_quantity").val(resp.small_quantity);
			$("#large_quantity").val(resp.large_quantity);
			$("#hostsitepickup_idFK").val($("#hsDropDown").val());
			pid = resp.hostsitepickup_idFK;
			$.get('/hsJSON', {}, function(response){
				var resp = JSON.parse(response);
				$.each(resp, function(i, item) {
					if(item.id == pid){
						
						$("#siteID").val(item.id);
					}
				});
			});
			$("#customerID").val(resp.fk_user_id);
			$("#orderID").val(order_id);
			$('html, body').animate({scrollTop:$('#scrollPosition').position().top}, 'slow');
		}
	});
	
}

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
			if(options[i].value == $("#hsDropDown").val()){
				createID = options[i].id;
				// alert("createID");
			}
		}
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
				hostSiteOrderID : distID,
				dateCreated : $("#creation_date").val(),
				donations : "",
				hostSitePickupID : $("#siteID").val(),
				totalPaid : paid,
				shouldSendNotifications : $("#email_notifications").val(),
				donationReceipt :"",
				firstName : $("#customer_first_name").val(),
				largeBoxQuantity : $("#large_quantity").val(),
				customerID :  $("#customerID").val()
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