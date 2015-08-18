<!DOCTYPE html>
<html lang="en">

	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<meta name="description" content="Garden Fresh Box">
		<meta name="author" content="Max Gardiner 2015">

		<title>Garden Fresh Box - Donate</title><link rel="shortcut icon" href="images/gfb.ico" type="image/x-icon"/ >

		<!-- Bootstrap Core CSS -->
		<link href="../css/bootstrap.min.css" rel="stylesheet">

		<!-- Custom CSS -->
		<link href="../css/custom.css" rel="stylesheet">
	</head>

	<body>

		<!-- jQuery -->
		<script src="js/jquery.js"></script>

		<!-- Bootstrap Core JavaScript -->
		<script src="js/bootstrap.min.js"></script>

		<!-- Helper Custom JavaScript -->
		<script src="js/helper.js"></script>

		<!-- Donate Custom JavaScript -->
		<script src="js/donate.js"></script>
		
		<!--  Validator JavaScript -->
		<script src="../js/validation.js"></script>

		<div class="body_div">

			<!-- header file containing the main nav bar and logo -->
			<%include file="../header.mako"/>
			<div class="row">
				<div id="sidebar" style="display: none;" class="col-sm-2">
					<%include file="../tools/sidebar.mako"/>
				</div>
				
				<div id="mainContent" class="col-sm-10">
				<h5 class="formA"> Currently our donations go through the CanadaHelps.org website. Just click the donate button and you may choose to donate specifically to the Garden Fresh Box program </h5> 
				<a href="https://www.canadahelps.org/dn/7869"><img style="margin-left:2em" src="/images/donate_button.png"></a>
					<div style="display:none" id="newAccount" class="wellA"> <!-- once canadagives website is open we may be able to get api? -->

					<div id = "hsAction"><h4 class="form">New Donation</h4></div><br>
					<div class="form-group">
						<div class="row">
							<div class="col-A">
								<h5 class="formA"> Contact Information </h5>
								<div class="input-group">
									<span id="customer_first_name_label" class="input-group-addonA">First Name</span>
									<input id="customer_first_name" type="text" class="form-controlA" placeholder="John" val="" required>
								</div>
								<div class="input-group">
									<span id="customer_last_name_label" class="input-group-addonA">Last Name</span>
									<input id="customer_last_name" type="text" class="form-controlA" placeholder="Doe" val="">
								</div>
								<div class="input-group">
									<span id="customer_email_label" class="input-group-addonA">Email</span>
									<input id="customer_email" type="email" class="form-controlA" placeholder="john.doe@example.com" val="">
								</div>
								<div class="input-group">
									<span id="customer_phone_label" class="input-group-addonA">Phone</span>
									<input id="customer_phone" type="text" class="form-controlA" placeholder="519-123-4567" val="">
								</div>
							</div>
							<div class="col-A">
								<h5 class="formA"> Donation Order </h5>
								<div class="input-group">
									<span id="donation_label" class="input-group-addonA">Donation Amount ($)</span>
									<input id="donation" type="text" class="form-controlA" placeholder="20" val="">
								</div>
								<div class="input-group text-left">
									<span id="donation_receipt_label" class="input-group">
										<p><br>
											Receive Donation Receipt via Email?   
											<input id="donation_receipt" type="checkbox" value="off" onchange="toggleReceipt()">
										</p>
									</span>
								</div>
								
								<br>
								<br>
								<br>
								<div class="input-group">
									<p id="error_box" class="errormsg"><p>
								</div>
							
						</div>
							<input id="confirmDonate" type="submit" onclick="confirmDonate()" class="button_general_left">
						</div>

					</div>
				</div>
				<!-- This is used to store the original id if the user is being edited-->
				<div style="display: none;">
					<input id="customer_id" type="text" class="form-control" val="">
				</div>
			</div>	

			<%include file="../footer.mako"/>

		</div><!--End of body_div-->


	</body>

</html>
