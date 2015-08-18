//get users table
$(window).load(function(){
	$.get('/user', {'email':'*'}, function(response){
		$("#allAccounts").html(response);
		addRowHandlers();
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


function changeRole(){
	role = $("#role").val();

	if (role=="Host Site Coordinator"){
		document.getElementById("associated-hostsite-area").style.display = 'block';
	}
	else{
		document.getElementById("associated-hostsite-area").style.display = 'none';
	}
}

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
	
	if($("#acctAction").html().indexOf('Edit Account</h4>') > -1){
		//this is an edit
	
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
		$.ajax({
			type: 'put',
			url: '/user',
			data: {
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
	
function addRowHandlers() {
	var table = document.getElementById("usersTable");
	var rows = table.getElementsByTagName("tr");
	
	for (i = 0; i < rows.length; i++) {
		var currentRow = table.rows[i];
		var createClickHandler = function(row) {
			return function() {
				load_user(row.id);
			};
		};
		currentRow.onclick = createClickHandler(currentRow);
	}
}

function load_user(user_id){
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
		}
		$("#first_name").val(resp.first_name);
		$("#last_name").val(resp.last_name);
		$("#email").val(resp.email);
		$("#oldEmail").val(resp.email);
		$("#phone").val(resp.phone_number);
		$("#password").val(resp.password);
		$.get('/hs', {'hostSiteID':resp.fk_hostsite_id}, function(response2){
			var resp2 = JSON.parse(response2);
			if (resp2 != null){
				
				$("#associated-site").val(resp2.name);
				$("#hostSite-id").val(resp.hostsite_id);
			}
		});
	});
}