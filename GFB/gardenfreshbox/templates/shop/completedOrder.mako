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

	<!--  Validator JavaScript -->
	<script src="../js/validation.js"></script>
	
	<div class="body_div">

			<!-- header file containing the main nav bar and logo -->
			<%include file="../header.mako"/>
			
			<div class="row">
				<div id="sidebar" style="display: none;" class="col-sm-2">
					<%include file="../tools/sidebar.mako"/>
				</div>
				<p>
				Thank you for your payment. Your transaction has been completed, and a receipt for your purchase has been emailed to you. You may log into your account at www.paypal.com to view details of this transaction.
				</p>
			</div>

			<%include file="../footer.mako"/>

		</div><!--End of body_div-->
	</body>

</html>
