$(window).load(function(){
	$("#submit").click(check_login)
});

//check_login - check if input is valid, if it is then add a new customer to database, and log user in
function check_login(){
	if (create_user_input_is_valid(false)){
		$.ajax({
			type: 'put',
			url: '/user',
			data: {
				email : $("#email").val(),
				password : $("#password").val(),
				first_name : $("#first_name").val(),
				last_name : $("#last_name").val(),
				role : 4,
				phone_number : $("#phone").val(),
				host_site : ""
			},
			complete: function(response) {
				if (response.success == "false"){
					alert(response.message);
				} else {
					alert($("#first_name").val() + " " + $("#last_name").val() + " added successfully");
					
					$.ajax({
						type: 'get',
						url: '/user/auth',
						data: {
							email : $("#email").val(),
							password : $("#password").val()
						},
						success: function(response) {
							//response will be JSON. response['success'] = false, message will have a list of bad fields
							var resp = JSON.parse(response);
							if(resp.success == "true"){
								window.location.href = '/';
							} else {
								alert("You have not been logged in. \n" +  resp.message)
							}
						}
					});
				}
			}
		});
	}
}
