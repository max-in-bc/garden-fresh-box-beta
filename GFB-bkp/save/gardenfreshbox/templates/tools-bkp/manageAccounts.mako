<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta name="description" content="Garden Fresh Box">
	<meta name="author" content="Fruitful Community Solutions">

	<title>Garden Fresh Box</title>

	<!-- Bootstrap Core CSS -->

	<link href="../css/bootstrap.min.css" rel="stylesheet">

	<!-- Custom CSS -->
	<link href="../css/custom.css" rel="stylesheet">
</head>

<body>

	<!-- jQuery -->
	<script src="../js/jquery.js"></script>
	<!-- Bootstrap Core JavaScript -->
	<script src="../js/bootstrap.min.js"></script>

	<div class="body_div">

			<!-- header file containing the main nav bar and logo -->
			<%include file="../header.mako"/>

			<div class="row">
				<div id="adminSidebar" style="display: none;" class="col-sm-2">
					<%include file="../tools/adminSidebar.mako"/>
				</div>

				<div id="mainContent" class="col-sm-10">
					<div class="content">
						<h2>Manage Accounts</h2>
						<div id="newAccount" class="wellA">
							<div id = "acctAction">
								<h4 class="form">New Account</h4>
							</div>
							<div class="row">
								<div class="col-A">
									<div class="form-group">
										<select id="role" class="form-controlB">
											<option>Administrator</option>
											<option>Coordinator</option>
										</select>

										<div class="input-group">
											<span class="input-group-addonA">First Name</span>
											<input id="first_name" type="text" class="form-controlA" placeholder="John">
										</div>

										<div class="input-group">
											<span class="input-group-addonA">Last Name</span>
											<input id="last_name" type="text" class="form-controlA" placeholder="Doe">
										</div>

										<div class="input-group">
											<span class="input-group-addonA">Email Address</span>
											<input id="email" type="text" class="form-controlA" placeholder="john.doe@example.com">
										</div>

										<div class="input-group">
											<span class="input-group-addonA">Phone Number</span>
											<input id="phone" type="text" class="form-controlA" placeholder="519-123-4567">
										</div>

										<div class="input-group">
											<span class="input-group-addonA">Password</span>
											<input id="password" type="password" class="form-controlA" placeholder="">
										</div>

										<br>
										<input id="submitNew" type="submit" class="button_general_left">

										<!-- This is used to store the original email address if the user is being edited-->
										<div style="display: none;">
											<input id="oldEmail" type="text" class="form-control" val="">
										</div>

									</div>
								</div> <!--col 6-->
							</div> <!-- row -->

						</div>
						<div id="allAccounts" class="well" style="background-color:white" >Loading ...</div>
					</div>		
				</div>
			</div>
			
			<%include file="../footer.mako"/>
		</div><!--End of body_div-->

		<script type="text/javascript">
		//get users table
		$(window).load(function(){
			$.get('/user', {'email':'*'}, function(response){
				$("#allAccounts").html(response);
				addRowHandlers();
			});
		});
		
		$("#submitNew").click(function(e){
			role = $("#role").val()
			if (role=="Coordinator"){
				role = 2;
			} else if (role=="Administrator") {
				role = 1;
			}
			if($("#acctAction").html() == '<h4 class="form">Edit Account</h4>'){
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
						phone_number : $("#phone").val()
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
		});
		</script>

		<script type="text/javascript">
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
				
				$.get('/user', {'email':email}, function(response){
					resp = JSON.parse(response)
					
					$("#acctAction").html("<h4>Edit Account</h4>");

					if (resp.role == 1){
						$("#role").val("Administrator");
					} else if (resp.role == 2){
						$("#role").val("Coordinator");
					}

					$("#first_name").val(resp.first_name);
					$("#last_name").val(resp.last_name);
					$("#email").val(resp.email);
					$("#oldEmail").val(resp.email);
					$("#phone").val(resp.phone_number);
					$("#password").val(resp.password);

				});
				

			}
		</script>

	</body>

</html