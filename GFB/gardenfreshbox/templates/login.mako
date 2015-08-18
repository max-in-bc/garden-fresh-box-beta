<!DOCTYPE html>
<html lang="en">

	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<meta name="description" content="Garden Fresh Box">
		<meta name="author" content="Max Gardiner 2015">

		<title>Garden Fresh Box - Login</title><link rel="shortcut icon" href="images/gfb.ico" type="image/x-icon"/ >

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

		<!-- Custom JavaScript -->
		<script src="js/login.js"></script>
		
		<!-- Validation JavaScript -->
		<script src="js/validation.js"></script>


		<div class="body_div">

			<!-- header file containing the main nav bar and logo -->
			<%include file="header.mako"/>

			<div class="content">
				<div class="login_page">
					<h1 class="login_page">Login</h1>
					<p class="content">
						Please enter your email address and password to log in.
					</p>
				</div>

				<!-- <div class="login_page"> -->
					<div class="login_page_form">
						<label id="email_label" class="form_label">Email address</label>
						<input class="form_label_box" type="text" id="email" size="55em" val="">
					</div>
					<div class="login_page_form">
						<label id="password_label" class="form_label">Password</label>
						<input class="form_label_box" type="password" id="password" size="55em" val="">
					</div>
					<div class="login_page_form">
						<p id="error_box" class="errormsg"><p>
					</div>
					<div class="login_button_div">
						<input id="submit" type="submit" class="button_general"/>
					</div>
				<!-- </div> -->
			</div>

			<%include file="footer.mako"/>

		</div><!--End of body_div-->

	</body>

</html>