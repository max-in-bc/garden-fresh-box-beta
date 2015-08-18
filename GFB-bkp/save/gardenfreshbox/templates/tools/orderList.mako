<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta name="description" content="Garden Fresh Box">
	<meta name="author" content="Fruitful Community Solutions">

	<title>Garden Fresh Box</title>

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

	<div class="body_div">
			<!-- header file containing the main nav bar and logo -->
			<%include file="../header.mako"/>

			<div class="row">
				<div id="sidebar" style="display: none;" class="col-sm-2">
					<%include file="../tools/sidebar.mako"/>
				</div>

				<div id="mainContent" class="col-sm-10">
					<div class="content">
						<h2>Master Order List</h2>
						<div id="list" class="well" style="background-color:white">Loading&hellip;</div>
					</div>
				</div>
			</div>

			<%include file="../footer.mako"/>
	</div><!--End of body_div-->

	<!-- Get table -->
	<script type="text/javascript">
		$(window).load(function(){
			$.get('/sales/cashsales', {'hostSiteName':"*"}, function(response) {
				$("#list").html(response);
			});
		});
	</script>

</body>

</html>