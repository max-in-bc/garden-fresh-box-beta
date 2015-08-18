
$(window).load(function(){
	$("#submit").click(check_login)
});

function check_login(){
	$.ajax({
		type: 'get',
		url: '/user/auth',
		data: {
			email : $("#username").val(),
			password : $("#password").val()
		},
		success: function(response) {
			//response will be JSON. response['success'] = false, message will have a list of bad fields
			var resp = JSON.parse(response);
			if(resp.success == "true"){
				window.location.href = '/dashboard';
			} else {
				alert("You have not been logged in. \n" +  resp.message)
			}
		}
	});
}