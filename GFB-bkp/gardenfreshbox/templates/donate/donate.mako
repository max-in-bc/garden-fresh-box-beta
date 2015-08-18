<!DOCTYPE html>
<html lang="en">

	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<meta name="description" content="Garden Fresh Box">
		<meta name="author" content="Fruitful Community Solutions">

		<title>Garden Fresh Box - Donate</title>

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

		<div class="body_div">

			<!-- header file containing the main nav bar and logo -->
			<%include file="../header.mako"/>
			<div class="row">
				<div id="sidebar" style="display: none;" class="col-sm-2">
					<%include file="../tools/sidebar.mako"/>
				</div>

				<div id="mainContent" class="col-sm-10">
					
					<div id="newAccount" class="wellA">

					<div id = "hsAction"><h4 class="form">New Donation</h4></div><br>
					<div class="form-group">
						<div class="row">
							<div class="col-A">
								<h5 class="formA"> Contact Information </h5>
								<div class="input-group">
									<span class="input-group-addonA">First Name</span>
									<input id="customer_first_name" type="text" class="form-controlA" placeholder="John" val="">
								</div>
								<div class="input-group">
									<span class="input-group-addonA">Last Name</span>
									<input id="customer_last_name" type="text" class="form-controlA" placeholder="Doe" val="">
								</div>
								<div class="input-group">
									<span class="input-group-addonA">Email Address</span>
									<input id="customer_email" type="text" class="form-controlA" placeholder="john.doe@example.com" val="">
								</div>
								<div class="input-group">
									<span class="input-group-addonA">Phone Number</span>
									<input id="phone" type="text" class="form-controlA" placeholder="519-123-4567" val="">
								</div>
							</div>
							<div class="col-A">
								<h5 class="formA"> Donation Order </h5>
								<div class="input-group">
									<span class="input-group-addonA">Donation Amount</span>
									<input id="donation" type="text" class="form-controlA" placeholder="20" val="">
								</div>
								<div class="input-group text-left">
									<span class="input-group">
										<p><br>
											Receive Donation Receipt?   
											<input id="donation_receipt" type="checkbox" value="off" onchange="toggleReceipt()">
										</p>
									</span>
								</div>

								<br>
								<br>
								<br>
								
							
						</div>
							<input id="confirmDonate" type="submit" class="button_general_left">
						</div>

					</div>
				</div>
			</div>	

			<%include file="../footer.mako"/>

		</div><!--End of body_div-->


	</body>

</html>
