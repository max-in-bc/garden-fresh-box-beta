<!DOCTYPE html>
<html lang="en">

	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<meta name="description" content="Garden Fresh Box">
		<meta name="author" content="Fruitful Community Solutions">

		<title>Garden Fresh Box - Contact Us</title>

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



		<div class="body_div">

			<!-- header file containing the main nav bar and logo -->
			<%include file="../header.mako"/>
			<div class="row">
				<div id="sidebar" style="display: none;" class="col-sm-2">
					<%include file="../tools/sidebar.mako"/>
				</div>

				<div id="mainContent" class="col-sm-10">
			
					<div class="content">
						<div>
							<h1>Contact Us</h1>
						</div>
						<div>
							<p>Have a question, comment, or concern?</p>
							<p>(519) 821-6638 ext. 344</p>
							<p><a href="mailto:gfbox@guelphchc.ca">gfbox@guelphchc.ca</a></p>
							<p>Guelph Community Health Centre<br>
							Attn: Garden Fresh Box<br>
							176 Wyndham St. N<br>
							Guelph, ON, N1H 8N9</p>
							<p> For information about pickup locations, please visit the <a href='/info'>info page</a> and scroll down to the "Locations" information. </p>
						</div>
					</div>
				</div>

			<%include file="../footer.mako"/>

		</div><!--End of body_div-->

	</body>

</html>
