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
	<!-- Bootstrap Core JavaScript -->
	<script src="../js/bootstrap.min.js"></script>
	<!-- Helper JavaScript -->
	<script src="../js/helper.js"></script>
	<!-- Manage Host Site JavaScript -->
	<script src="../js/manageHS.js"></script>
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
					<div class="content">
						<h2>Manage Host Sites</h2>
						<div id="newAccount" class="wellA">
							<div id = "hsAction">
								<h4 class="form interior">New Host Site</h4>
							</div>
							<div class="row">
								<div class="col-sm-12">
									<div class="form-group">

										<div class="row interior">
											<div class="col-A">
												<div class="input-group">

													<span id="HSname_label" class="input-group-addonA">Name</span>
													<input id="HSname" type="text" class="form-controlA" placeholder="Host Site" val="">
												</div>

												<div class="input-group">
													<span id="phone_label" class="input-group-addonA">Phone</span>
													<input id="phone" type="text" class="form-controlA" placeholder="519-123-4567" val="">
												</div>
												
												<div class="input-group">
													<span id="email_label" class="input-group-addonA">Email</span>
													<input id="email" type="text" class="form-controlA" placeholder="myname@myhostsite.com" val="">
												</div>

												<!-- address -->
												<h5 class="formA">Address</h5>
												<div class="input-group">
													<span id="address_label" class="input-group-addonA">Address</span>
													<input id="address" type="text" class="form-controlA" placeholder="123 Fake St." val="">
												</div>
												<div class="input-group">
													<span id="city_label" class="input-group-addonA">City</span>
													<input id="city" type="text" class="form-controlA" placeholder="Guelph" val="">
												</div>
												<div class="input-group">
													<span id="province_label" class="input-group-addonA">Province</span>
													<input id="province" type="text" class="form-controlA" placeholder="Ontario" val="">
												</div>
												<div class="input-group">
													<span id="postal_code_label" class="input-group-addonA">Postal Code</span>
													<input id="postal_code" type="text" class="form-controlA" placeholder="A1B 2C3" val="">
												</div>
											</div>
										
											<div class="col-A">
												<!-- hours -->
												<h5 class="formA">Hours</h5>
												<div class="input-group">
													<span id="monHrs_label" class="input-group-addonA">Monday</span>
													<input id="monHrs" type="text" class="form-controlA" placeholder="9am - 5pm" val="">
												</div>
												<div class="input-group">
													<span id="tuesHrs_label" class="input-group-addonA">Tuesday</span>
													<input id="tuesHrs" type="text" class="form-controlA" placeholder="9am - 5pm" val="">
												</div>
												<div class="input-group">
													<span id="wedHrs_label" class="input-group-addonA">Wednesday</span>
													<input id="wedHrs" type="text" class="form-controlA" placeholder="9am - 5pm" val="">
												</div>
												<div class="input-group">
													<span id="thursHrs_label" class="input-group-addonA">Thursday</span>
													<input id="thursHrs" type="text" class="form-controlA" placeholder="9am - 5pm" val="">
												</div>
												<div class="input-group">
													<span id="friHrs_label" class="input-group-addonA">Friday</span>
													<input id="friHrs" type="text" class="form-controlA" placeholder="9am - 5pm" val="">
												</div>
												<div class="input-group">
													<span id="satHrs_label" class="input-group-addonA">Saturday</span>
													<input id="satHrs" type="text" class="form-controlA" placeholder="9am - 5pm" val="">
												</div>
												<div class="input-group">
													<span id="sunHrs_label" class="input-group-addonA">Sunday</span>
													<input id="sunHrs" type="text" class="form-controlA" placeholder="9am - 5pm" val="">
												</div>
											</div>
										</div>
										<div id="scrollPosition"></div> <!-- this is the location to scroll to -->
										
										<br>
										<input id="submit" type="submit" class="button_general_left">
										<input id="newhostsite" type="button" class="button_general_left" value="New Host Site">
										<div class="input-group">
											<p id="error_box" class="errormsg"><p>
										</div>
										<!-- This is used to store the original email address if the user is being edited-->
										<div style="display: none;">
											<input id="hostSiteID" type="text" class="form-control" val="">
										</div>

									</div>
								</div> <!--col 6-->
							</div> <!-- row -->

						</div>
						<div id="allHS" class="well" style="background-color:white" >Loading ...</div>
					</div>		
				</div>
			</div>
			
			<%include file="../footer.mako"/>
		</div><!--End of body_div-->

	</body>

</html>