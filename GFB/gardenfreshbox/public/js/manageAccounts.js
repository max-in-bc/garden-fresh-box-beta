//on page load:
//	Get all accounts and add them to the list with row/sort handlers to load the data to editing form
//	Add appropriate host site info to the associated host site dropdown
$(window).load(function(){
	$.get('/user', {'email':'*','sortid':"Last Name"}, function(response){
		$("#allAccounts").html(response);
		addRowHandlers("usersTable", sortTable, load_user);
		setupFilter();
	});

	
	$.get('/hsJSON', {}, function(response){
		var resp = JSON.parse(response);
		$("#associated-site").append("<option id=NULL>--Select--</option>")
		
		$.each(resp, function(i, item) {
			$("#associated-site").append("<option id=" + item.id + ">" + item.name + "</option>")
		});
	 });	

	$('#role').change(changeRole);
	$('#associated-site').change(changeSite);
});

//changeRole - If an account is selected as a host site coordinator they must select a valid hs to associate with
function changeRole(){
	role = $("#role").val();

	if (role=="Host Site Coordinator"){
		document.getElementById("associated-hostsite-area").style.display = 'block';
	}
	else{
		$("#associated-site").val("--Select--")
		document.getElementById("associated-hostsite-area").style.display = 'none';
	}
}

//changeSite - If a different site is selected from the dropdown, the id is added to hidden div for further use
function changeSite(){
	$.get('/hsJSON', {}, function(response){
		var resp = JSON.parse(response);
		$.each(resp, function(i, item) {
			
			if (item.name == $("#associated-site").val()){
				$("#hostSite-id").val(item.id);
			}
		});
	});
}
	
//manageAccount - Check if inputs are valid, then if a user has been selected from the list update their info with form data; otherwise create a new account with form data
function manageAccount(){
	var host_site_id;
	role = $("#role").val()

	if (role=="Regular User"){
		role = 4;
	}
	else if (role=="Host Site Coordinator"){
		role = 3;
	} else if (role=="Administrator") {
		role = 2;
	}
	
	if (create_user_input_is_valid(true)){
		if($("#acctAction").html().indexOf('Edit Account</h4>') > -1){
			//Edit an existing user
			
			$.ajax({
				type: 'put',
				url: '/user',
				data: {
					new_email : $("#email").val(),
					email : $("#oldEmail").val(),
					password : $("#password").val(),
					first_name : $("#first_name").val(),
					last_name : $("#last_name").val(),
					role : role,
					phone_number : $("#phone").val(),
					host_site : $("#hostSite-id").val()
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
		} else {
			
			//Add a New User
			$.ajax({
				type: 'put',
				url: '/user',
				data: {
					new_email : $("#email").val(),
					email : $("#email").val(),
					password : $("#password").val(),
					first_name : $("#first_name").val(),
					last_name : $("#last_name").val(),
					role : role,
					phone_number : $("#phone").val(),
					host_site : $("#hostSite-id").val()
				},
				complete: function(response) {
					if (response.success == "false"){
						alert(response.message);
					} else {
						alert($("#first_name").val() + " " + $("#last_name").val() + " added successfully");
							location.reload();
						}
				}
			});
		}
	}
}
	
//sortTable - custom sorting function for the account management table
function sortTable(sortid){
	$.get('/user', {'email':'*','sortid':sortid}, function(response){
		var filtertext = $("#filterbox").val()
		$("#allAccounts").html(response);
		addRowHandlers("usersTable", sortTable, load_user);
		setupFilter();
		$("#filterbox").val(filtertext);
		$("#filterbox").keyup();
	});

}

//load_user - when a row has been selected from the table, highlight it and add data to form
function load_user(user_id){
	try{

		$("#allAccounts").removeClass("active");
		$("#" + user_id).addClass("active");
		$("#" + user_id).siblings().removeClass("active");
		
		
		
		var row = document.getElementById(user_id);
		emailCell = row.cells[3];
		email = emailCell.valueOf().innerHTML;
	
		var host_id;
		$.get('/user', {'email':email}, function(response){
			resp = JSON.parse(response)
			
			$("#acctAction").html("<h4>Edit Account</h4>");
			if (resp.fk_credentials == 2 || resp.fk_credentials == 1){
				$("#role").val("Administrator");
				changeRole();
			} else if (resp.fk_credentials == 3){
				$("#role").val("Host Site Coordinator");
				changeRole();
			}else if (resp.fk_credentials == 4){
				$("#role").val("Regular User");
				changeRole();
			}
			$("#first_name").val(resp.first_name);
			$("#last_name").val(resp.last_name);
			$("#email").val(resp.email);
			$("#oldEmail").val(resp.email);
			$("#phone").val(resp.phone_number);
			$("#password").val(resp.password);
			$.get('/hs', {'hostSiteID':resp.fk_hostsite_id, 'staticTable':'false'}, function(response2){
				var resp2 = JSON.parse(response2);
				if (resp2 != null){
					
					$("#associated-site").val(resp2.name);
					$("#hostSite-id").val(resp.hostsite_id);
				}
			});
		});

		$('#password-area').hide();
		changeSite();
		
		//move screen to top
		$('html, body').animate({scrollTop:$('#scrollPosition').position().top}, 'slow');
	}catch(e){
		
	}
}

//deleteClicked - Admin selected to delete an existing account, confirm and delete account on confirmation
function deleteClicked(event){
	if (confirm('Are you sure you want to delete this record?')) {

		var user_id = event.target.id.split("_")[1];
		$.ajax({
			type: 'put',
			url: '/user',
			data: {
				id : user_id,
				email : "",
				password : "",
				first_name : "",
				last_name : "",
				role : "",
				phone_number : "",
				host_site : ""
			},
			complete: function(response) {
				if (response.success == "false"){
					alert(response.message);
				} else {
					alert("Record deleted successfully");
					location.reload();
				}
			}
		});
	} 

}
	