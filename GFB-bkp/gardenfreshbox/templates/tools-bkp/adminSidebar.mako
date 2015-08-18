<nav>
	<div class="sidebar-nav navbar-left" role ="navigation">
		<h4>Administrator Tools</h4>
		<ul class="nav nav-pills nav-stacked">
			<li id="hostsites" class="" role="presentation"><a href="/hostsites">Manage Host Sites</a></li>
			<li id="accounts" class="" role="presentation"><a href="/accounts">Manage Accounts</a></li>
			<li id="masterorders" class="" role="presentation"><a href="/masterorders">Master Order List</a></li>
			<li id="donors" class="" role="presentation"><a href="/donors">Master Donation List</a></li>
			<li id="mastercustomers" class="" role="presentation"><a href="/mastercustomers">Master Customer List</a></li>
		</ul>
		<h4>Host Site Tools</h4>
		<ul class="nav nav-pills nav-stacked">
			<li id="cashsales" class="" role="presentation"><a href="/cashsales">Cash Sales</a></li>
			<li id="distOrders" class="" role="presentation"><a href="/distribution">Orders to Distribute</a></li>
		</ul>
	</div>
</nav>

<script type="text/javascript">
	$(window).load(function(){
		var e = document.getElementById('adminSidebar');
		$.get('/user/me', {}, function(response){
			if(response==''){
				//user is not logged in
				e.style.display = 'none';
				document.getElementById('mainContent').className='col-sm-12';
			} else{
				var me = JSON.parse(response);
				if(me.role == 1 || me.role == 2){
					e.style.display = 'block';
					document.getElementById('mainContent').className='col-sm-10';
				} else {
					e.style.display = 'none';
					document.getElementById('mainContent').className='col-sm-12';
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