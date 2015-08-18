<!DOCTYPE html>
<html lang="en">

	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<meta name="description" content="Garden Fresh Box">
		<meta name="author" content="Fruitful Community Solutions">

		<title>Garden Fresh Box - Login</title>

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
						<label class="form_label">Email address</label>
						<input class="form_label_box" type="text" id="username" size="55em" val="">
					</div>
					<div class="login_page_form">
						<label class="form_label">Password</label>
						<input class="form_label_box" type="password" id="password" size="55em" val="">
					</div>
					<!-- <input id="submit" type="submit" class="btn btn-submit"> -->
					<div class="login_button_div">
						<input id="submit" type="submit" class="button_general"/>
					</div>
			</div>

			<%include file="footer.mako"/>

		</div><!--End of body_div-->

	<script type="text/javascript">
		$("#submit").click(function(e) {
			$.ajax({
				type: 'get',
				url: '/user/auth',
				data: {
					email : $("#username").val(),
					password : $("#password").val()
				},
				success: function(response) {
					//response will be JSON. response['success'] = false, message will have a list of bad fields
					var resp = JSON.parse(response);
					if(resp.success == "true"){
						window.location.href = '/dashboard';
					} else {
						alert("You have not been logged in. \n" +  resp.message)
					}
				}
			});
		});
	</script>


	</body>

</html>