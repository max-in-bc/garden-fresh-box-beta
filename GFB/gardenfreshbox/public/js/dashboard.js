//on window load:
//	Add correct links to each button
//	Hide/Show correct buttons depending on admin level
$(window).load(function(){
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
	$("#editprofileButton").click(function(e){
		window.location.href = '/editprofile';
	});
	$("#changepasswordButton").click(function(e){
		window.location.href = '/changepassword';
	});
	
	var e = document.getElementById('dashboard');
	$.get('/user/me', {}, function(response){
	
		if(response!=''){
			e.style.display = 'block';
			var me = JSON.parse(response);
			
			if(me.role == 3){
				document.getElementById("admin-controls").style.display = "none";
				document.getElementById('admin-controls').className='col-sm-12';
				document.getElementById("hostsite-controls").style.display = "block";
			} 
			else if(me.role == 4){
				document.getElementById("hostsite-controls").style.display = "none";
				document.getElementById('hostsite-controls').className='col-sm-12';
				document.getElementById("user-controls").style.display = "block";
			} 
		}
	});
	
	var curr = /[^/]*$/.exec(window.location.href)[0];
	
	var ele = document.getElementById(curr.valueOf());
	
	if (ele != null){
		ele.className='active';
	}
	
});

