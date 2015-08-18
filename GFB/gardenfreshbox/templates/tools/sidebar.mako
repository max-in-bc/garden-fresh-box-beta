<nav>
	<div class="sidebar-nav navbar-left" role ="navigation">
	
		<div id="user-controls">
			<h4>User Tools</h4>
			<ul class="nav nav-pills nav-stacked">
				<li id="yourOrders" class="" role="presentation"><a href="/currentorders">Your Current Orders</a></li>
				<li id="yourdonations" class="" role="presentation"><a href="/currentdonations">Your Donations</a></li>
				<li id="changepassword" class="" role="presentation"><a href="/changepassword">Change Password</a></li>
				<li id="editinfo" class="" role="presentation"><a href="/editprofile">Edit Personal Information</a></li>
			</ul>

			<div id="hostsite-controls">
				<h4>Host Site Tools</h4>
				<ul class="nav nav-pills nav-stacked">
<!-- 					<li id="cashsales" class="" role="presentation"><a href="/cashsales">Cash Sales</a></li> -->
					<li id="distOrders" class="" role="presentation"><a href="/distribution">Manage Orders</a></li>
					<li id="hostsites" class="" role="presentation"><a href="/hostsites">Edit Host Site Details</a></li>
							
				</ul>
			
					<div id="admin-controls">
						<h4>Administrator Tools</h4>
						<ul class="nav nav-pills nav-stacked">
							<li id="accounts" class="" role="presentation"><a href="/accounts">Manage Accounts</a></li>
							<li id="masterorders" class="" role="presentation"><a href="/masterorders">Master Order List</a></li>
							<li id="donors" class="" role="presentation"><a href="/donors">Master Donation List</a></li>
							<li id="mastercustomers" class="" role="presentation"><a href="/mastercustomers">Master Customer List</a></li>
							<li id="pickupdates" class="" role="presentation"><a href="/pickupdates">Manage Pickup Dates</a></li>
							<li id="sampleboxes" class="" role="presentation"><a href="/managesamples">Manage Sample Boxes</a></li>
						</ul>
					</div>
				</div>
			</div>
	</div>
</nav>

<script type="text/javascript">
	$(window).load(function(){
		var e = document.getElementById('sidebar');
		$.get('/user/me', {}, function(response){
			if(response==''){
				//user is not logged in
				e.style.display = 'none';
				document.getElementById('mainContent').className='col-sm-12';
			} else{
				e.style.display = 'block';
				document.getElementById('mainContent').className='col-sm-10';
				
				var me = JSON.parse(response);
				
				if(me.role == 3){
					var role = document.getElementById('admin-controls');
					role.style.display = 'none';
					document.getElementById('mainContent').className='col-sm-12';
					
					role = document.getElementById('hostsite-controls');
					role.style.display = 'block';
					document.getElementById('mainContent').className='col-sm-10';
				} 
				else if(me.role == 4){
					var role = document.getElementById('hostsite-controls');
					role.style.display = 'none';
					document.getElementById('mainContent').className='col-sm-12';
					
					role = document.getElementById('user-controls');
					role.style.display = 'block';
					document.getElementById('mainContent').className='col-sm-10';
				} 
			}
		});

		var curr = /[^/]*$/.exec(window.location.href)[0];
		
		var ele = document.getElementById(curr.valueOf());
		if (ele != null){
			ele.className='active';
		}

	});
</script>