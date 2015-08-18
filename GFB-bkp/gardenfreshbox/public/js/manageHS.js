//get users table
$(window).load(function(){
	$.get('/hs', {'hostSiteID':'*'}, function(response){
		$("#allHS").html(response);
		addRowHandlers();
	});

	$("#submit").click(manageSite);
});


function manageSite(){
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
				phone : $("#phone").val()
			},
			complete: function(response) {
				if (response.success == "false"){
					alert(response.message);
				} else {
					alert($("#HSname").val() + " updated successfully")
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
				phone : $("#phone").val()
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

function addRowHandlers() {
	var table = document.getElementById("hsTable");
	var rows = table.getElementsByTagName("tr");
	for (i = 0; i < rows.length; i++) {
		var currentRow = table.rows[i];
		var createClickHandler = function(row) {
			return function() {
				load_hs(row.id);
			};
		};
		currentRow.onclick = createClickHandler(currentRow);
	}
}

function load_hs(hostSiteID){
	var row = document.getElementById(hostSiteID);
	
	$.get('/hs', {'hostSiteID':hostSiteID}, function(response){
		var resp = JSON.parse(response)
		
		$("#hsAction").html("<h4>Edit Host Site</h4>");
		$("#hostSiteID").val(hostSiteID);

		$("#HSname").val(resp.name);
		$("#address").val(resp.address);
		$("#city").val(resp.city);
		$("#province").val(resp.province);
		$("#postal_code").val(resp.postal_code);
		$("#phone").val(resp.phone_number);

		var ops = resp.hours_of_operation;

		$("#monHrs").val(ops.monday);
		$("#tuesHrs").val(ops.tuesday);
		$("#wedHrs").val(ops.wednesday);
		$("#thursHrs").val(ops.thursday);
		$("#friHrs").val(ops.friday);
		$("#satHrs").val(ops.saturday);
		$("#sunHrs").val(ops.sunday);

	});
}