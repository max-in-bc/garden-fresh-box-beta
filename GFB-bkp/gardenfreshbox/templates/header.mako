<div class="header">
	<div class="logo_image">
		<a href="/">
			<img src="../images/BannerImage.jpg">
		</a>
	</div>
	<div class="regular_nav">
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
		<p id="name" class="text-right" style="height:10px;margin-top:10px;margin-right:20px;"></p>
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