//on window load:
//	Populate form with user data
//	If user is host site coordinator then show dropdown with associated host site; also locked
$(window).load(function(){
	
	$.get('/user/me', {}, function(response){
		me = JSON.parse(response);
		var user_email = me.email;
		
		var host_site = me.host_site;
		role = me.role;
		
		
		$.get('/user', {'email':user_email}, function(response){
			
			resp = JSON.parse(response)
				
			$("#first_name").val(resp.first_name);
			$("#last_name").val(resp.last_name);
			$("#email").val(resp.email);
			$("#oldEmail").val(resp.email);
			$("#password").val(resp.password);
			$("#phone").val(resp.phone_number);
			if (resp.fk_credentials == 4){ 
				document.getElementById("associated-hostsite-area").style.display = 'none';
				document.getElementById("hostSite").innerHTML = "";
				$("#role").val("Regular User");
				
			}
			
			else if (resp.fk_credentials == 3){ 
				$.get('/hs', {'hostSiteID':host_site}, function(response){
					var resp = JSON.parse(response)
					document.getElementById("hostSite").innerHTML = resp.name;
				});
					
				document.getElementById("associated-hostsite-area").style.display = 'block';
				$("#role").val("Host Site Coordinator");
				
			}

			else if ((resp.fk_credentials == 2)||(resp.fk_credentials == 1)){ 
				document.getElementById("associated-hostsite-area").style.display = 'none';
				document.getElementById("hostSite").innerHTML = "";
				$("#role").val("Administrator");
			}
				
		});
	});

});

//toggleEmail - Change boolean value when user turns on/off donation reciept option
function toggleEmail(){
	var caller = document.getElementById("email_notifications");
	if (caller.value == "on"){
		caller.value = "off";
	} else {
		caller.value = "on";
	}
}
		
//editProfile - check if inputs are valid, if they are then change the user's profile to the form data
function editProfile(){
	if (create_user_input_is_valid(true)){
		$.ajax({
			type: 'put',
			url: '/user',
			data: {
				new_email : $("#email").val(),
				email : $("#oldEmail").val(),
				password : $("#oldEmail").val(),
				first_name : $("#first_name").val(),
				last_name : $("#last_name").val(),
				role : role,
				host_site : $("#hostSite").val(),
				phone_number : $("#phone").val()
			},
			complete: function(response) {
				if (response.success == "false"){
					alert(response.message);
				} else {
					alert($("#first_name").val() + " " + $("#last_name").val() + " updated successfully");
					location.reload();
				}
			}
		});
	}
}
