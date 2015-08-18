var email1, password1, first_name1, last_name1, role1, phone_number1;

//on page load:
//	Get logged in user info and update name to page
$(window).load(function(){
	$.get('/user/me', {}, function(response){

		if(response!=''){
			var me = JSON.parse(response);
			document.getElementById('changepw').innerHTML = "Change password for ".concat(me.user_name);
		
			email1 = me.email;
			password1 = me.password;
			first_name1 = me.first_name;
			last_name1 = me.last_name;
			role1 = me.role;
			phone_number1 = me.phone_number;
		}
	});

	$("#submit").click(changePassword);
});
		
//changePassword - check if inputs are valid, if they are then update new password to database
function changePassword(){
	
	if (change_password_input_is_valid(email1)){
		var o_password = $('#old_password').val();
		var n_password = $('#new_password').val();
		$.ajax({
			type: 'put',
			url: '/user/cp',
			data: {
				email : email1,
				oldPassword : o_password,
				newPassword : n_password
			},
			complete: function(response) {
				if (response.success == "false"){
					alert('failure');
				} else {
					alert("Your password was updated successfully");
					location.reload();
				}
			}
		});
	}
	
}