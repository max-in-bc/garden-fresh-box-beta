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
	<!-- Bootstrap Core JavaScript -->
	<script src="../js/masterCustList.js"></script>
	<!-- Bootstrap Core JavaScript -->
	<script src="../js/helper.js"></script>
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
						<h2>Master Customer List</h2>
						<h3 id="subheader">Click any order before the first Friday of the order's delivery month to edit it, as long as you did not already pay</h3>
				
						<div id="newAccount" class="wellA interior" >

						<div id = "hsAction"><h4 class="form">Edit Your Order</h4></div><br>
						<div id="editOrderScrollPosition"></div> <!-- this is the location to scroll to -->
						
						<div class="form-group">
							<div class="row">
								<div class="col-A">
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
										<div class="input-group">
											<span id="creation_date_label" class="input-group-addonA" disabled>Date Created</span>
											<input id="creation_date" type="date" class="form-controlA" placeholder="" val="" style="width:40%;">
										</div>
										<br>
									<div style="display:none" class="input-group text-left">
										<span class="input-group">
										<p><br>Receive Email notifications?   
											<input id="email_notifications" type="checkbox" value="off" onchange="toggleEmail()">
										</p>
										</span>
									</div>
									<br>
									
								</div>
	
								<div class="col-A">
									<div class="input-group">
										<span id="site_and_date_label" class="input-group-addonA2">Pickup Location and Date</span>
										<select id="hostsitepickup_idFK" class="form-controlB"></select>
										<select id="distribution_date" class="form-controlB"></select>
									</div>
									<div class="input-group">
										<span id="small_quantity_label" class="input-group-addonA">Number Small</span>
										<input id="small_quantity" type="text" class="form-controlA" placeholder="0" val="">
									</div>
									<div class="input-group">
										<span id="large_quantity_label" class="input-group-addonA">Number Large</span>
										<input id="large_quantity" type="text" class="form-controlA" placeholder="0" val="">
									</div>
									<p><br>This has been paid  
										<input id="is_paid" type="checkbox" value="off">
									</p>
									<div style="display:none;"  class="input-group">
										<span id="total_paid_label" class="input-group-addonA">Amt. Paid</span>
										<input id="total_paid" type="text" class="form-controlA" placeholder="0" val="">
									</div>
									<div style="display:none;"  class="input-group">
										<span id="donation_label" class="input-group-addonA">Donation Amt.</span>
										<input id="donation" type="text" class="form-controlA" placeholder="0" val="">
									</div>
									<div style="display:none" class="input-group text-left">
										<span class="input-group">
										<p><br>Receive Donation Receipt?   
											<input id="donation_receipt" type="checkbox" value="off" onchange="toggleReceipt()">
										</p>
										</span>
									</div>
									
								</div>
								
										
										<input id="submit" type="submit" class="button_general_left" onclick="placeOrder()">
										
										<div class="input-group">
									<p id="error_box" class="errormsg"><p>
								</div>
							</div> <!-- close row -->
						
							<!-- This is used to store the original email address if the user is being edited-->
							<div style="display: none;">
								<input id="orderID" type="text" class="form-control" val="">
								<input id="siteID" type="text" class="form-control" val="">
								<input id="customerID" type="text" class="form-control" val="">
							</div>
						</div> <!-- close form group -->
					</div> <!-- close well -->
					
						
						<div id="customerList" class="well" style="background-color:white">Loading&hellip;</div>
						
						<div id="allOrders" class="well" style="background-color:white" >Select a customer to view/edit their orders</div>
						<div id="userOrdersScrollPosition"></div> <!-- this is the location to scroll to -->
						
					</div>
				</div>
			</div>

			<%include file="../footer.mako"/>
	</div><!--End of body_div-->
</body>

</html>