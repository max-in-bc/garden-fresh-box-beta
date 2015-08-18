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
		<link href="css/bootstrap.min.css" rel="stylesheet">

		<!-- Custom CSS -->
		<link href="css/custom.css" rel="stylesheet">
	</head>

	<body>
		<!-- jQuery -->
		<script src="js/jquery.js"></script>
		<!-- Bootstrap Core JavaScript -->
		<script src="js/bootstrap.min.js"></script>

		<div class="row">
			<div class="body_div">
				<!-- header file containing the main nav bar and logo -->
				<%include file="header.mako"/>
				<div id="sidebar" style="display: none;" class="col-sm-2">
					<%include file="/tools/sidebar.mako"/>
				</div>

				<div id="mainContent" class="col-sm-10">
					<div class="content">
						<div class="hero_image">
							<img src="../images/GCHC.jpg" class="hero_image">					
						</div>
						<!-- <div><h1>HomePage</h1></div> -->
						<div class="summary_buttons">
						<p class="intro"><span class="intro">T</span>he Garden Fresh Box Program is a non-profit, fresh produce buying service created to help people access affordable fresh fruits and vegetables and also to support our local farmers.</p>
						
							<div class="summary_end">
								<a href="/shop/buy">
									<div class="summary_button" id="summary_buy_garden_fresh_box">						
										<div class="summary_heading">
											<h2 class="summary_button">
												Buy a Garden Fresh Box
											</h2>
										</div>
									</div>
								</a>
								<div class="summary_description">
									<p class="summary_button">
										Shop for a Garden Fresh Box for yourself or your family.
										<br>
										<a href="/shop/buy">
										Learn More
										</a>
									</p>
								</div>
							</div>

							<div class="summary_mid">
								<a href="/info">
									<div class="summary_button" id="summary_about_garden_fresh_box">						
										<div class="summary_heading">
											<h2 class="summary_button">
												About the Program
											</h2>
										</div>	
									</div>
								</a>
								<div class="summary_description">					
									<p class="summary_button">
										Learn more about the Garden Fresh Box Program and how we're helping Guelph.
										<br>
										<a href="/info">
											Learn More
										</a>
									</p>
								</div>
							</div>

							<div class="summary_end">
								<a href="/contact">
									<div class="summary_button" id="summary_feedback_image">						
										<div class="summary_heading">
											<h2 class="summary_button">
												Leave Feedback
											</h2>
										</div>										
									</div>
								</a>
								<div class="summary_description">
									<p class="summary_button">
										Are we doing a good job? Let the community know by leaving some feedback!
										<br>
										<a href="/contact">
											Learn More
										</a>
									</p>
								</div>			
							</div>
						</div><!-- End of summary buttons -->
					</div><!-- End of the content div -->
				</div>
				<%include file="footer.mako"/>
			</div> <!-- end of body div-->
		</div> <!-- end of row -->


	</body>

</html>
