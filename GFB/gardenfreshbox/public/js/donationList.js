//On window load:
//	Populate list with donors
$(window).load(function(){
	$.get('/sales/donors', {}, function(response) {
		$("#list").html(response);
		setupFilter();
	});
});