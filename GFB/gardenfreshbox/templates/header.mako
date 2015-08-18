<div class="header">
	<div>
		<div float="right" class="logo_image">
	<!-- 		<a href="http://www.guelphchc.ca/" target="_blank"><img  class="header_image" src="../images/GuelphCHCLogo.png"></a> -->
	<!-- 		<a href="http://www.children.gov.on.ca/" target="_blank"><img  class="header_image" src="../images/MinistryOfChildrenAndYouthServices.png"></a> -->
			
			<a href="/">
				<img class="header_image" style="width:18%" src="../images/veg_circle_2.jpeg">
			</a>
	<!-- 		<a href="http://www.waterloowellingtonlhin.on.ca/" target="_blank"><img  class="header_image" src="../images/WaterlooWellingtonLocalHealthNetwork.png"></a> -->
	<!-- 		<a href="http://www.ontariochc.org/" target="_blank"><img  class="header_image" src="../images/OntarioCommunityHealth.png"></a> -->
		</div>
	</div>
	<div class="regular_nav">
		<div class="inner_nav">
			<ul class="regular_nav">
				<li class="regular_nav">
					<a href="/">Home</a>
				</li>
				<li class="regular_nav">
					<a href="/info">Info</a>
				</li>
				<li class="regular_nav">
					<a href="/shop/buy">Buy</a>
				</li>
				<li class="regular_nav">
					<a href="/donate">Donate</a>
				</li>
				<li class="regular_nav">
					<a href="/contact">Contact Us</a>
				</li>
			</ul>
		</div>
		<p id="name" class="text-right" style="margin-top:10px;margin-right:20px;color:rgb(53,118,193);"></p>
	
	</div>
</div>

<script type="text/javascript">
	//get user information to see if they are logged in
	$(window).load(function(){
		$.get('/user/me', {}, function(response){
			if(response==''){
				$("#name").html("");
			} else{
				var me = JSON.parse(response);
				//me.user_name = the user's email address
				var e = document.getElementById('name');	
				$("#name").html("Hello " + me.user_name);
			}
		});
	});
</script>