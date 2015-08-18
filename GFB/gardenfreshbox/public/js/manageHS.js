//on page load:
//	Get all host site and add them to the list with row/sort handlers to load the data to editing form
//	Add appropriate host site info to the associated host site dropdown
$(window).load(function(){
	$.get('/hs', {'hostSiteID':'*', 'staticTable':'false', 'sortid':'Name'}, function(response){
		$("#allHS").html(response);
		addRowHandlers("hsTable", sortTable, load_hs);
		setupFilter();
	});
	
	$.get('/user/me', {}, function(response){

		if(response!=''){
			var me = JSON.parse(response);
			if (me.role == "3"){
				$("#hostSiteID").val(me.host_site);
				load_hs(me.host_site)
				$("#newhostsite").hide();
				$("#allHS").hide();
			}
			else{
				$("#newhostsite").click(newSiteButtonClick);
				$(".interior").hide();
			}
		}
	});
	
	$("#submit").click(manageSite);
	
});

//newSiteButtonClick - open the dropdown for a new host site form and clear all
function newSiteButtonClick() {
	$("#hsAction").html("<h4 class=\"form\">New Host Site</h4>");
	$("#hostSiteID").val("");

	$("#HSname").val("");
	$("#address").val("");
	$("#city").val("");
	$("#province").val("");
	$("#postal_code").val("");
	$("#phone").val("");
	$("#email").val("");


	$("#monHrs").val("");
	$("#tuesHrs").val("");
	$("#wedHrs").val("");
	$("#thursHrs").val("");
	$("#friHrs").val("");
	$("#satHrs").val("");
	$("#sunHrs").val("");
	
	$(".interior").show();
	$("#newhostsite").hide();
}

//manageSite - check if input is valid, if it is then update the currently selected host site with form data or add new host site if none selected
function manageSite(){
	if (create_hostsite_input_is_valid()){
		if($("#hsAction").html().indexOf('Edit Host Site</h4>') > -1){
			//this is an edit
			$.ajax({
				type: 'put',
				url: '/hs',
				data: {
					hostSiteID : $("#hostSiteID").val(),
					name : $("#HSname").val(),
					address : $("#address").val(),
					city : $("#city").val(),
					province : $("#province").val(),
					postalCode : $("#postal_code").val(),
					hoursOfOperation : "{\"monday\":\"" + $("#monHrs").val() + "\",\"tuesday\":\"" + $("#tuesHrs").val() +"\",\"wednesday\":\"" + $("#wedHrs").val()+ "\",\"thursday\":\"" + $("#thursHrs").val() +"\",\"friday\":\"" + $("#friHrs").val() +"\",\"saturday\":\"" + $("#satHrs").val() + "\",\"sunday\":\"" + $("#sunHrs").val() + "\"}",
					phone : $("#phone").val(),
					email : $("#email").val()
				},
				complete: function(response) {
					if (response.success == "false"){
						alert(response.message);
					} else {
						alert($("#email").val() + " updated successfully")
						location.reload();
					}
				}
			});
		} else {
			$.ajax({
				type: 'put',
				url: '/hs',
				data: {
					hostSiteID : "",
					name : $("#HSname").val(),
					address : $("#address").val(),
					city : $("#city").val(),
					province : $("#province").val(),
					postalCode : $("#postal_code").val(),
					hoursOfOperation : "{\"monday\":\"" + $("#monHrs").val() + "\",\"tuesday\":\"" + $("#tuesHrs").val() +"\",\"wednesday\":\"" + $("#wedHrs").val()+ "\",\"thursday\":\"" + $("#thursHrs").val() +"\",\"friday\":\"" + $("#friHrs").val() +"\",\"saturday\":\"" + $("#satHrs").val() + "\",\"sunday\":\"" + $("#sunHrs").val() + "\"}",
					phone : $("#phone").val(),
					email : $("#email").val()
				},
				complete: function(response) {
					if (response.success == "false"){
						alert(response.message);
					} else {
						alert($("#HSname").val() + " added successfully")
						location.reload();
					}
				}
			});
		}
	}
}

//sortTable - custom sort function for host site list
function sortTable(sortid){
	$.get('/hs', {'hostSiteID':'*', 'staticTable':'false', 'sortid':sortid}, function(response){
		var filtertext = $("#filterbox").val()
		$("#allHS").html(response);
		addRowHandlers("hsTable", sortTable, load_hs);
		setupFilter();
		$("#filterbox").val(filtertext);
		$("#filterbox").keyup();
	});
}

//load_hs - load the data from selected host site to the form
function load_hs(hostSiteID){
	$("#allHS").removeClass("active");
	$("#" + hostSiteID).addClass("active");
	$("#" + hostSiteID).siblings().removeClass("active");
	
	
	$(".interior").show();
	$("#newhostsite").show();
	
	var row = document.getElementById(hostSiteID);
	
	$.get('/hs', {'hostSiteID':hostSiteID, 'staticTable':'false'}, function(response){
		var resp = JSON.parse(response)
		$("#hsAction").html("<h4 class=\"form\">Edit Host Site</h4>");
		$("#hostSiteID").val(hostSiteID);

		$("#HSname").val(resp.name);
		$("#address").val(resp.address);
		$("#city").val(resp.city);
		$("#province").val(resp.province);
		$("#postal_code").val(resp.postal_code);
		$("#phone").val(resp.phone_number);
		$("#email").val(resp.email);

		var ops = resp.hours_of_operation;

		$("#monHrs").val(ops.monday);
		$("#tuesHrs").val(ops.tuesday);
		$("#wedHrs").val(ops.wednesday);
		$("#thursHrs").val(ops.thursday);
		$("#friHrs").val(ops.friday);
		$("#satHrs").val(ops.saturday);
		$("#sunHrs").val(ops.sunday);

	});
	$('html, body').animate({scrollTop:$('#scrollPosition').position().top}, 'slow');
}

//deleteClicked - admin selected delete button for a selected record, confirm delete, then remove from backend
function deleteClicked(event){
	if (confirm('Are you sure you want to delete this record?')) {
		var site_id = event.target.id.split("_")[1];
		$.ajax({
			type: 'put',
			url: '/hs',
			data: {
				hostSiteID : site_id,
				name : "",
				address : "",
				city : "",
				province : "",
				postalCode : "",
				hoursOfOperation : "",
				phone : "",
				email : ""
			},
			complete: function(response) {
				if (response.success == "false"){
					alert(response.message);
				} else {
					alert("Record deleted successfully");
					location.reload();
				}
			}
		});
	}
}