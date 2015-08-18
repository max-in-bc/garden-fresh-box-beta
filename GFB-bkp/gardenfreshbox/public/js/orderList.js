$(window).load(function(){
	$.get('/sales/cashsales', {'hostSiteName':"*"}, function(response) {
		$("#list").html(response);
	});
});