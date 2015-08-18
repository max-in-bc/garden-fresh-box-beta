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
	<script src="../js/helper.js"></script>
	<script src="../js/sampleBoxes.js"></script>


	<div class="body_div">
			<!-- header file containing the main nav bar and logo -->
			<%include file="../header.mako"/>

			<div class="row">
				<div id="sidebar" style="display: none;" class="col-sm-2">
					<%include file="../tools/sidebar.mako"/>
				</div>

				<div id="mainContent" class="col-sm-10">
				
				<div class="content">
						<h2>Add/Edit Garden Fresh Box Samples</h2>
						<div id="newAccount" class="wellA">
							<div id = "sampleAction">
								<h4>Enter a new sample item</h4>
							</div>
							<div class="row">
								<div class="col-sm-12">
									<div class="form-group">

										<div class="row">
												<div class="input-group">
													<span class="input-group-addonA">Small box item to add:</span>
													<input id="newSmallItem" type="text" class="form-controlA" placeholder="4lbs potatoes" val="">
												</div>
												<div class="input-group">
													<span class="input-group-addonA">Large box item to add:</span>
													<input id="newLargeItem" type="text" class="form-controlA" placeholder="1.5lbs potatoes" val="">
												</div>
												<br>
												<p style="margin-left:12px">Note you can leave fields blank if you only wish to add to one of the boxes</p>
											</div>
										</div>
										<div id="scrollPosition"></div> <!-- this is the location to scroll to -->
								
										<input id="submit" type="submit" class="button_general_left">
										
										<!-- This is used to store the original email address if the user is being edited-->
										<div style="display: none;">
											<input id="smallID" type="text" class="form-control" val="">
											<input id="largeID" type="text" class="form-control" val="">
										</div>
									</div>
							</div> <!-- row -->

						</div>
					<div class="content">
						<h4>Click on a sample to edit it...</h4>
						<div id="sampleBoxes" class="well" style="background-color:white">Loading&hellip;</div>
					</div>
					
					
				</div>
			</div>

			<%include file="../footer.mako"/>
	</div><!--End of body_div-->
</body>

</html>