//on page load:
//	load orders table with list of all orders
$(window).load(function(){
	$.get('/sales/cashsales', {'hostSiteName':"*", 'orderID': ""}, function(response) {
		$("#list").html(response);
		addRowHandlers("ordersTable", null, load_hs_page);
		setupFilter();
	});
});

//load_hs_page - user selected a host site, so open the host site details page with this host site selected
//	Note: this is done by temporarily giving the admin host site credentials and then changing it immediately back on the page load
function load_hs_page(site_id){
	$.ajax({
		type: 'put',
		url: '/user/me',
		data: {
			siteID :  site_id,
			changed: "true"
		},
		complete: function(response) {
			if (response.success == "false"){
				alert(response.message);
			}
			else{
				window.open("/distribution","_self")
			}
		}
	});
}