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
				<div id="adminSidebar" style="display: none;" class="col-sm-2">
					<%include file="../tools/adminSidebar.mako"/>
				</div>

				<div id="mainContent" class="col-sm-10">
					<div class="content">
						<h2>Orders to Distribute</h2>
						<div class="input-group col-sm-4">
							<span class="form-controlC">Host Site</span>
							<select id="hsDropDown" class="form-controlB1" onchange="loadSales()"></select>
						</div><br>
						<div id="list" class="well" style="background-color:white">Select A Host Site</div>
					
					</div>

				</div>
			</div>

			<%include file="../footer.mako"/>
	</div><!--End of body_div-->

	<!-- Get table -->
	<script type="text/javascript">
		$(window).load(function(){
			$.get('/hsJSON', {}, function(response){
				var resp = JSON.parse(response);
				$("#hsDropDown").append("<option id=NULL>--Select--</option>")
				$.each(resp, function(i, item) {
					if(item.name != "Online"){
						$("#hsDropDown").append("<option id=" + item.id + ">" + item.name + "</option>")
					}
				});
			});
		});
		function loadSales(){
			if ($("#hsDropDown").val() == "--Select--"){
				$("#list").html("Select A Host Site");
			} else {
				$.get('/sales/dist', {'hostSiteName':$("#hsDropDown").val()}, function(response){
					$("#list").html(response);
				});
			}
		}
	</script>

</body>

</html>