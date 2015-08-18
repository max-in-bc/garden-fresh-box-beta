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
				<%include file="sidebar.mako"/>
			</div>

			<div id="mainContent" class="col-sm-10">
				<h2>Program Administrator Tools</h2>

				<div class="btn-group btn-group-justified" role="group" aria-label="...">
					<!-- First Admin Column -->
					<div class="col-sm-3">
						<div class="btn-group" role="group">
							<button id="hostsitesButton" type="button" style="height:200px;width:230px;margin-bottom:4px;white-space:normal;background-color:rgba(232,228,218,0.3);" class="btn btn-default">
								<h4>Manage Host Sites</h4>
								<ul class="text-left">
									<li>Create new Host Sites</li>
									<li>Add and remove Host Site Coordinators from Host Sites</li>
									<li>Modify Hours of Operation and Host Site Contact Information</li>
								</ul>
							</button>
						</div>
						<div class="btn-group" role="group">
							<button id="mastercustomersButton" type="button" style="height:200px;width:230px;margin-bottom:4px;white-space:normal;background-color:rgba(232,228,218,0.3);" class="btn btn-default">
								<h4>Master Customer List</h4>
								<ul class="text-left">
									<li>View a list of all customers who have purchased a Garden Fresh Box</li>
									<br><br><br>
								</ul>
							</button>
						</div>
					</div>

				  <!-- Second Admin Column -->
					<div class="col-sm-3">
						<div class="btn-group" role="group">
							<button id="accountsButton" type="button" style="height:200px;width:230px;margin-bottom:4px;white-space:normal;background-color:rgba(232,228,218,0.3);" class="btn btn-default">
								<h4>Manage Accounts</h4>
								<ul class="text-left">
									<li>Create, edit and view Accounts for Host Site Coordinators and Program Administrators</li>
									<li>Add and remove Host Site Cooridnators from Host Sites</li>
								</ul>
							</button>
						</div>
						<div class="btn-group" role="group">
							<button id="masterordersButton" type="button" style="height:200px;width:230px;margin-bottom:4px;white-space:normal;background-color:rgba(232,228,218,0.3);" class="btn btn-default">
								<h4>Master Order List</h4>
								<ul class="text-left">
									<li>View a list of all orders to be distributed organized by host site based on a selected upcoming date</li>
									<br><br>
								</ul>
							</button>
						</div>
					</div>		

					<!-- third admin column -->
					<div class="col-sm-3">
						<div class="btn-group" role="group">
							<button id="donorsButton" type="button" style="height:200px;width:230px;margin-bottom:4px;white-space:normal;background-color:rgba(232,228,218,0.3);" class="btn btn-default">
								<h4>Donors List</h4>
								<ul class="text-left">
									<li>View a list of contact information for doners who have donated more than $20 to the Garden Fresh Box Program</li>
									<br><br>
								</ul>
							</button>
						</div>
					</div>
				</div> <!-- close admin button group -->

				<h2>Host Site Tools</h2>

				<div class="btn-group btn-group-justified" role="group" aria-label="...">
					<div class="col-sm-3">
					<div class="btn-group" role="group">
						<button id="cashsalesButton" type="button" style="height:200px;width:230px;margin-bottom:4px;white-space:normal;background-color:rgba(232,228,218,0.3);" class="btn btn-default">
							<h4>Cash Sales</h4>
							<ul class="text-left">
								<li>Add a new cash sale for the selected host site</li>
								<li>Edit an existing Cash Sale</li>
								<li>Cancel a Cash Sale made at the host site</li>
								<br>
							</ul>
						</button>
					</div>
				  </div>
				  
				  <div class="col-sm-3">
					<div class="btn-group" role="group">
						<button id="distributionButton" type="button" style="height:200px;width:230px;margin-bottom:4px;white-space:normal;background-color:rgba(232,228,218,0.3);" class="btn btn-default">
							<h4>Orders To Distribute</h4>
							<ul class="text-left">
								<li>View a list of Orders to be distributed based on a chosen distribution day</li>
								<li>Contains the names and contact information for clients who will be picking up an Order</li><br>
							</ul>
						</button>
					</div>
				  </div>
				</div> <!-- close host site button group -->
				
			</div> <!-- close main content -->
		</div> <!-- close row -->

	<%include file="../footer.mako"/>
	</div><!--End of body_div-->

	<script type="text/javascript">
		$("#hostsitesButton").click(function(e){
			window.location.href = '/hostsites';
		});
		$("#accountsButton").click(function(e){
			window.location.href = '/accounts';
		});
		$("#masterordersButton").click(function(e){
			window.location.href = '/masterorders';
		});

		$("#mastercustomersButton").click(function(e){
			window.location.href = '/mastercustomers';
		});
		$("#donorsButton").click(function(e){
			window.location.href = '/donors';
		});

		$("#cashsalesButton").click(function(e){
			window.location.href = '/cashsales';
		});
		$("#customersButton").click(function(e){
			window.location.href = '/customers';
		});
		$("#distributionButton").click(function(e){
			window.location.href = '/distribution';
		});
	</script>

	</body>

</html>