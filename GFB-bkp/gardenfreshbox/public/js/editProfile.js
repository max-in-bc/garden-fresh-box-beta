$(window).load(function(){
	$.get('/user/me', {}, function(response){
		me = JSON.parse(response);
		var user_email = me.email;

		$.get('/user', {'email':user_email}, function(response){
			resp = JSON.parse(response)

			$("#first_name").val(resp.first_name);
			$("#last_name").val(resp.last_name);
			$("#email").val(resp.email);
			$("#oldEmail").val(resp.email);
			$("#phone").val(resp.phone_number);
			if (resp.fk_credentials == 4){ 
				document.getElementById("associated-hostsite-area").style.display = 'none';
				document.getElementById("hostSite").innerHTML = "";
				$("#role").val("Regular User");
				
			}
			
			else if (resp.fk_credentials == 3){ 
				document.getElementById("associated-hostsite-area").style.display = 'block';
				document.getElementById("hostSite").innerHTML = "test2";
				$("#role").val("Host Site Coordinator");
				
			}

			else if ((resp.fk_credentials == 2)||(resp.fk_credentials == 1)){ 
				document.getElementById("associated-hostsite-area").style.display = 'none';
				document.getElementById("hostSite").innerHTML = "";
				$("#role").val("Administrator");
			}
				
		});
	});

	$("#submit").click(editProfile);
});

function toggleEmail(){
	var caller = document.getElementById("email_notifications");
	if (caller.value == "on"){
		caller.value = "off";
	} else {
		caller.value = "on";
	}
}
		
function editProfile(){
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
