$(window).load(function(){
	$("#submit").click(check_login)
});

//check_login - check if input is valid, if it is then log user in 
function check_login(){
	if(login_input_is_valid()){
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
