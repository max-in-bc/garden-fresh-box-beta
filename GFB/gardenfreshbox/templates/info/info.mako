<!DOCTYPE html>
<html lang="en">

	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<meta name="description" content="Garden Fresh Box">
		<meta name="author" content="Max Gardiner 2015">

		<title>Garden Fresh Box - Information</title><link rel="shortcut icon" href="images/gfb.ico" type="image/x-icon"/ >

		<!-- Bootstrap Core CSS -->
		<link href="../css/bootstrap.min.css" rel="stylesheet">

		<!-- Custom CSS -->
		<link href="../css/custom.css" rel="stylesheet">
			<style>
				table, th, td {
					border: 1px solid black;
					border-collapse: collapse;
				}
				th, td {
					padding: 5px;
				}
			</style>
	</head>

	<body>

		<!-- jQuery -->
		<script src="js/jquery.js"></script>

		<!-- Bootstrap Core JavaScript -->
		<script src="js/bootstrap.min.js"></script>
		<!-- Custom JavaScript -->
		<script src="js/info.js"></script>

		<div class="body_div">
			<!-- header file containing the main nav bar and logo -->
			<%include file="../header.mako"/>

			<div class="row">
				<div id="sidebar" style="display: none;" class="col-sm-2">
					<%include file="../tools/sidebar.mako"/>
				</div>

				<div id="mainContent" class="col-sm-10">
					<div class="content">
						<h1>About Garden Fresh Box</h1>
						<p>The Garden Fresh Box Program is a non-profit, fresh produce buying service created to help people access affordable fresh fruits and vegetables and also to support our local farmers. We are affiliated with the Guelph Wellington Local Food. It is delivered to their neighbourhood on the third Wednesday of the month. Payment must be received at the site no later than noon on the first Friday of the month.</p>
						<div class="videoWrapper">
							<iframe src="https://www.youtube.com/embed/Sg0JUw77cro" frameborder="0" allowfullscreen></iframe>
						</div>
						<h1>How to Order a Box</h1>
						<p>To order a box, simply navigate and click the "Buy" link on the top bar of this page, and fill in the required information.</p>
						
						<p>Garden Fresh Box contents are seasonal. Produce included is based on quality and availability. The Garden Fresh Box content changes from month to month because the fruits and vegetables are chosen in season when they are at the peak of their nutritional value.</p>
							
						<div>
							<h1>Sample Boxes</h1>
							<div id="sampleBoxes" class="" style="background-color:white">Loading&hellip;</div>
						</div>
						
						<div>
							<h1>Due &amp; Delivery Dates</h1>
							<div id="pickupDates" class="" style="background-color:white">Loading&hellip;</div>
						</div>
						
						<h1>Locations</h1>
						<div id="allHS" class="well" style="background-color:white" >Loading ...</div>

					</div>
				</div>
			</div>
			<%include file="../footer.mako"/>
		</div>

	</body>

</html>
