<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta name="description" content="Garden Fresh Box">
	<meta name="author" content="Max Gardiner 2015">

	<title>Garden Fresh Box</title><link rel="shortcut icon" href="images/gfb.ico" type="image/x-icon"/>

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
	
	<!-- New Order Custom JavaScript -->
	<script src="../js/newOrder.js"></script>

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
					<div id="newAccount" class="wellA">
						
						<div id = "hsAction"><h4 class="form">New Order</h4></div><br>
						<form name="payform" method="POST" onsubmit="return create_new_order_input_is_valid();" action="https://www.paypal.com/cgi-bin/webscr" id="payform" ><input type="hidden" name="cmd" value="_xclick">
						<input type="hidden" name="business" value="gfbox@guelphchc.ca">
						<input type="hidden" name="item_name" value="Garden Fresh Box">
						<input type="hidden" name="item_number" value="">
						<input type="hidden" name="no_shipping" value="1">
						<input type="hidden" name="return" value="http://gardenfreshbox.ca/shop/buy">
						<input type="hidden" name="currency_code" value="CAD">
						<input type="hidden" name="lc" value="CA">
												
						<input type="text" id="Editbox2" size="8" name="amount" value="" onFocus="this.blur" hidden="" readonly>
						
												
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
											<span id="creation_date_label" class="input-group-addonA">Date Created</span>
											<input id="creation_date" type="date" class="form-controlA" placeholder="" val="" style="width:40%;">
										</div>
										<br>
										<div style="display:none;" class="input-group text-left">
											<span class="input-group">
											<p>Recieve Email notifications?   
												<input id="email_notifications" type="checkbox" value="off" onchange="toggleEmail()">
											</p>
											</span>
										</div>

<!-- 										<div class="input-group"> -->
<!-- 											<span id="creation_date_label" >Date</span> -->
<!-- 											<input id="creation_date" type="date" class="form-control" placeholder="" val="" style="width:60%"> -->
<!-- 										</div> -->
										
									</div>
		
									<div class="col-A">
										<div class="input-group">
											<span id="site_and_date_label" class="input-group-addonA2">Pickup Location and Date</span>
											<select id="hostsitepickup_idFK" class="form-controlB"></select>
											<select id="distribution_date" class="form-controlB"></select>
										</div>
										<div class="input-group">
											<span id="small_quantity_label" class="input-group-addonA">Number Small</span>
											<input id="small_quantity" name="smallamount" type="text" class="form-controlA" placeholder="0" val="" onKeyUp="val = this.value;val = val * 15;otherval = this.form.largeamount.value * 20;this.form.amount.value=val + otherval;">
										</div>
										<div class="input-group">
											<span id="large_quantity_label" class="input-group-addonA">Number Large</span>
											<input id="large_quantity" name="largeamount" type="text" class="form-controlA" placeholder="0" val="" onKeyUp="val = this.value;val = val * 20;otherval = this.form.smallamount.value * 15;this.form.amount.value=val + otherval;">
										</div>
										<div style="display:none;"  class="input-group">
											<span id="total_paid_label" class="input-group-addonA">Amt. Paid</span>
											<input id="total_paid" type="text" class="form-controlA" placeholder="0" val="">
										</div>
										<div style="display:none;"  class="input-group">
											<span id="donation_label" class="input-group-addonA">Donation Amt.</span>
											<input id="donation" type="text" class="form-controlA" placeholder="0" val="">
										</div>
										<div style="display:none;" class="input-group text-left">
											<span class="input-group">
											<p><br>Receive Donation Receipt?   
												<input id="donation_receipt" type="checkbox" value="off" onchange="toggleReceipt()">
											</p>
											</span>
										</div>
										<br>
										<div id="payment_area">
									
									     	<span class="input-group"><input type="radio" name="payment-radio" value="Pay in person" checked> Pay in person</span>
									        <span class="input-group"><input type="radio" name="payment-radio" value="Pay online"> Pay online</span><br>
							
																						
											
											<input id="paypal_submit" type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_buynowCC_LG.gif" class="button_general_left" onclick="placeOrder(this)">
											<input id="paylater_submit" type="submit" class="button_general_left" onclick="placeOrder(this)">
										
										</div>
									</div>
									
									<div class="input-group">
										<p id="error_box" class="errormsg"><p>
									</div>
								</div> <!-- close row -->
								<!-- This is used to store the original id if the user is being edited-->
								<div style="display: none;">
									<input id="customer_id" type="text" class="form-control" val="">
								</div>
							</div> <!-- close form group -->
							</form>
					</div> <!-- close well -->
				</div> <!-- close main content -->
			</div>

			<%include file="../footer.mako"/>

		</div><!--End of body_div-->
	</body>

</html>
