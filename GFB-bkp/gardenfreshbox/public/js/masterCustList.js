$(window).load(function(){
	$.get('/sales/customers', {}, function(response) {
		$("#list").html(response);
	});
});