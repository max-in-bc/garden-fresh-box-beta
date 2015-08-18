//on page load:
//	Load the pickup dates to non-editable table
//	Load the sample boxes to non-editable table
//	Load the host sites to non-editable table
$(window).load(function(){
	$.get('/sales/dates', {'dateID':'*', "staticTable":"false"}, function(response) {
		$("#pickupDates").html(response);
	});
	
	$.get('/sales/samples', {'id':'*', 'staticTable':'false'} , function(response) {
		$("#sampleBoxes").html(response);
	});
	
	$.get('/hs', {'hostSiteID':'*', 'staticTable':'true', 'sortid':"Name"}, function(response){
		$("#allHS").html(response);
	});

});
