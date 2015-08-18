<div class="footer">

	<div class="footer_main">

		<div class="footer_contact">
			<div class="contact_us_heading">
				<h2 class="contact_us_heading">
					Contact Us:
				</h2>
			</div>
			<div class="contact_us_info">
				<p class="contact_us">
					Phone: (519) 821-6638 ext. 344<br>
					Email: <a href="mailto:gfbox@guelphchc.ca?Subject=Garden%20Fresh%20Box%20Feedback" target="_top">gfbox@guelphchc.ca</a><br>
					Mailing: 176 Wyndham St. N, Guelph, ON, N1H 8N9
					<br>
				</p>
			</div>
		</div>
		<div ">
			<div id="login" class="footer_login" >
				<a href="/login" class="footer_login">
					<!-- <button class="btn btn-default">Login</button> -->
					Login
				</a>
			</div>
			
			<div id="signup" class="footer_login">
				<a href="/signup" class="footer_login">
					Sign Up
				</a>
			</div>
		</div>

		<div id="logout" class="footer_login">
			<a class="footer_login" id="logout_button" style="cursor:pointer;"> Logout </a>
		</div>
	</div>

	<div class="footer_images">
		<a href="http://www.guelphchc.ca/" target="_blank"><img src="../images/GuelphCHCLogo.png" class="footer_images"></a>
		<a href="http://www.children.gov.on.ca/" target="_blank"><img src="../images/MinistryOfChildrenAndYouthServices.png" class="footer_images"></a>
		<a href="/"><img style="max-width:13%" src="../images/veg_circle.jpeg" class="footer_images"></a>
		<a href="http://www.waterloowellingtonlhin.on.ca/" target="_blank"><img src="../images/WaterlooWellingtonLocalHealthNetwork.png" class="footer_images"></a>
		<a href="http://www.ontariochc.org/" target="_blank"><img src="../images/OntarioCommunityHealth.png" class="footer_images"></a>
		
	
	</div>

	<script type="text/javascript">
		//get user information to see if they are logged in
		$(window).load(function(){
			$.get('/user/me', {}, function(response){
				if(response==''){
					//user is not logged in, ensure login is available
					var e = document.getElementById('login');
					e.style.display = 'footer_login';
					var e = document.getElementById('signup');
					e.style.display = 'footer_login';
					var e = document.getElementById('logout_button');
					e.style.display = 'none';
				} else{
					var me = JSON.parse(response);
					var e = document.getElementById('login');
					e.style.display = 'none';
					var e = document.getElementById('signup');
					e.style.display = 'none';
					var e = document.getElementById('logout');
					e.style.display = 'footer_login';
				}
			});
		});

		$("#logout_button").click(function(e){
			$.get('/user/logout', {}, function(response){
				alert("You have been logged out.");
				window.location.href = '/';
			});
		});
	</script>
	<script src="https://apis.google.com/js/client:platform.js" async defer></script>
</div>