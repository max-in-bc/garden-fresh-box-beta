$(window).load(function(){
	var host_site, host_site_name;
	$.get('/user/me', {}, function(response){
	
		if(response!=''){
			var me = JSON.parse(response);
			if (me.host_site != '' && me.role == 3){
				
				host_site = me.host_site;
			}
		}
	});
	
	$.get('/hsJSON', {}, function(response){
		var resp = JSON.parse(response);
		$("#hsDropDown").append("<option id=NULL>--Select--</option>")
		$.each(resp, function(i, item) {
			if(item.name != "Online"){
				$("#hsDropDown").append("<option id=" + item.id + ">" + item.name + "</option>")
				if (item.id == host_site){
					host_site_name = item.name;
					$("#hsDropDown").val(host_site_name);
					loadSales();
				    document.getElementById("hsDropDown").disabled=true;
				}
			}
		});
	});
});

function loadSales(){
	if ($("#hsDropDown").val() == "--Select--"){
		$("#list").html("Select A Host Site");
	} else {
		$.get('/sales/dist', {'hostSiteName':$("#hsDropDown").val()}, function(response){
			$("#list").html(response);
		});
	}
}