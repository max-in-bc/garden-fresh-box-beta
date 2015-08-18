$(window).load(function(){
	$.get('/sales/donors', {}, function(response) {
		$("#list").html(response);
	});
});