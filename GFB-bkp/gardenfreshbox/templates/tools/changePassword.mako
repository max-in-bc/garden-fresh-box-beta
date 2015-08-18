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
	<script src="../js/bootstrap.min.js"></script>
	<script src="../js/changePassword.js"></script>

	<div class="body_div">

			<!-- header file containing the main nav bar and logo -->
			<%include file="../header.mako"/>

			<div class="row">
				<div id="sidebar" style="display: none;" class="col-sm-2">
					<%include file="../tools/sidebar.mako"/>
				</div>

				<div id="mainContent" class="col-sm-10">
					
					<div id="newAccount" class="wellA">
					<h2 class="form" id="pageheader"><br></h2>
						<div><h4 class="formA" id = "changepw"></h4></div><br>

						<div class="form-group">
							<div class="row">
								<div class="col-A">
									
									
									<div class="input-group">
										<span class="input-group-addonA">Current Password</span>
										<input id="old_password" type="text" class="form-controlA" placeholder="John" val="">
									</div>
									<div class="input-group">
										<span class="input-group-addonA">New Password</span>
										<input id="new_password" type="text" class="form-controlA" placeholder="Doe" val="">
									</div>
									<div class="input-group">
										<span class="input-group-addonA">New Password</span>
										<input id="new_password_confirm" type="text" class="form-controlA" placeholder="john.doe@example.com" val="">
									</div>
									
								<br>
									<input id="submit" type="submit" class="button_general_left">
							</div> <!-- close row -->

							<!-- This is used to store the original email address if the user is being edited-->
							<div style="display: none;">
								<input id="orderID" type="text" class="form-control" val="">
							</div>
						</div> <!-- close form group -->
					</div> <!-- close well -->

				</div> <!-- close main content -->
			</div>
			
			<%include file="../footer.mako"/>
		</div><!--End of body_div-->

	</body>

</html>