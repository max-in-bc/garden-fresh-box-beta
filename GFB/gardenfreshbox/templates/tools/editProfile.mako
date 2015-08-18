<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta name="description" content="Garden Fresh Box">
	<meta name="author" content="Max Gardiner 2015">

	<title>Garden Fresh Box</title><link rel="shortcut icon" href="images/gfb.ico" type="image/x-icon"/ >

	<!-- Bootstrap Core CSS -->
	<link href="../css/bootstrap.min.css" rel="stylesheet">
	<!-- Custom CSS -->
	<link href="../css/custom.css" rel="stylesheet">


</head>

<body>

	<!-- jQuery -->
	<script src="../js/jquery.js"></script>
	<script src="../js/bootstrap.min.js"></script>
	<script src="../js/editProfile.js"></script>
	<script src="../js/validation.js"></script>

	<div class="body_div">

			<!-- header file containing the main nav bar and logo -->
			<%include file="../header.mako"/>

			<div class="row">
				<div id="sidebar" style="display: none;" class="col-sm-2">
					<%include file="../tools/sidebar.mako"/>
				</div>

				<div id="mainContent" class="col-sm-10">
					<div class="content">
						<h2>Manage Accounts</h2>
						<div id="newAccount" class="wellA">
							<div id = "acctAction">
								<h4 class="form">Edit Account Information</h4>
							</div>
							<div class="row">
								<div class="col-A">
									<div class="form-group">
										<select id="role" class="form-controlB" disabled="disabled">
											<option>Administrator</option>
											<option>Host Site Coordinator</option>
											<option>Regular User</option>
										</select>
											
										<div class="input-group">
											<span id="first_name_label" class="input-group-addonA">First Name</span>
											<input id="first_name" type="text" class="form-controlA" placeholder="John">
										</div>

										<div class="input-group">
											<span id="last_name_label" class="input-group-addonA">Last Name</span>
											<input id="last_name" type="text" class="form-controlA" placeholder="Doe">
										</div>

										<div class="input-group">
											<span id="email_label" class="input-group-addonA">Email Address</span>
											<input id="email" type="text" class="form-controlA" placeholder="john.doe@example.com">
										</div>

										<div class="input-group">
											<span id="phone_label" class="input-group-addonA">Phone Number</span>
											<input id="phone" type="text" class="form-controlA" placeholder="519-123-4567">
										</div>
										
										<div class="input-group">
											<span id="password_label" class="input-group-addonA">Password</span>
											<input id="password" type="password" class="form-controlA" disabled="true" placeholder="">
										</div>
										

										<div style="display: none;" class="input-group text-left">
											<span class="input-group">
												<p><br>
													Receive Email Notifications and Reminders?   
													<input id="email_notifications" type="checkbox" value="off" onchange="toggleEmail()">
												</p>
											</span>
										</div>
										
										<div class="input-group" id="associated-hostsite-area">
											<span id="hostSite_label" >Associated Host Site</span>
											<p id="hostSite" style="font-weight: bold"></p>
										</div>

										<br>
										<input id="submitNew" type="submit" class="button_general_left" onclick="editProfile()">

										<!-- This is used to store the original email address if the user is being edited-->
										<div style="display: none;">
											<input id="oldEmail" type="text" class="form-control" val="">
										</div>

									</div>
								</div> <!--col 6-->
								<div class="col-A">
									<div class="form-group">
										<div class="input-group">
											<p id="error_box" class="errormsg"><p>
										</div>
									</div>
								</div>
							</div> <!-- row -->

						</div>
					</div>	
					
				</div> <!-- close main content -->
			</div>
			
			<%include file="../footer.mako"/>
		</div><!--End of body_div-->

	</body>

</html>