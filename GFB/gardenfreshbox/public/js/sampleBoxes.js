//on page load:
//	load sample boxes to table
$(window).load(function(){
	$.get('/sales/samples', {"id":"*", 'staticTable':'true'} , function(response) {
		$("#sampleBoxes").html(response);
		addRowHandlers("samplesTable", null, load_sample);
	});
	
	$("#submit").click(manageSamples);
});

//manageSamples - add or edit large and small items in the sample boxes
//	Note small items and large items are added separately (each item is a single record in backend table)
function manageSamples(){
	
	if($("#sampleAction").html().indexOf('Edit existing samples</h4>') > -1){
		
		//this is an edit of small item
		if ($("#newSmallItem").val() != null && $("#newSmallItem").val() != ""){
			//this is an edit
			$.ajax({
				type: 'put',
				url: '/sales/samples',
				data: {
					id : $("#smallID").val(),
					item : $("#newSmallItem").val(),
					is_small_box : "1",
				},
				complete: function(response) {
					if (response.success == "false"){
						alert(response.message);
						location.reload();
					} 
				}
			});
		}
		if ($("#newLargeItem").val() != null && $("#newLargeItem").val() != ""){
			//this is an edit of large item
			$.ajax({
				type: 'put',
				url: '/sales/samples',
				data: {
					id : $("#largeID").val(),
					item : $("#newLargeItem").val(),
					is_small_box : "0",
				},
				complete: function(response) {
					if (response.success == "false"){
						alert(response.message);
					} else {
						alert("Sample updated successfully")
						location.reload();
					}
				}
			});
		}
	} else {
		//this is an add of small item
		if ($("#newSmallItem").val() != null && $("#newSmallItem").val() != ""){
			$.ajax({
				type: 'put',
				url: '/sales/samples',
				data: {
					id : $("#smallID").val(),
					item : $("#newSmallItem").val(),
					is_small_box : "1",
				},
				complete: function(response) {
					if (response.success == "false"){
						alert(response.message);
						location.reload();
					} 
				}
			});
		}
		if ($("#newLargeItem").val() != null && $("#newLargeItem").val() != ""){
			$.ajax({
				type: 'put',
				url: '/sales/samples',
				data: {
					id : $("#largeID").val(),
					item : $("#newLargeItem").val(),
					is_small_box : "0",
				},
				complete: function(response) {
					if (response.success == "false"){
						alert(response.message);
					} else {
						alert("Sample added successfully")
						location.reload();
					}
				}
			});
		}
	}
}

//load_sample - user selected an row in table, load the two samples that are on that row to the form
function load_sample(sampleID){
	try{
		$("#sampleBoxes").removeClass("active");
		$("#" + sampleID).addClass("active");
		$("#" + sampleID).siblings().removeClass("active");
	}catch(e){
		$("#sampleBoxes").removeClass("active");
	}
	
	//id contains the element id
	if (sampleID.split('_')[0] != "?"){ //if it is on a row with a blank value
		$.get("/sales/samples", {"id":sampleID.split('_')[0], "staticTable":"true"}, function(response) {
			var resp = JSON.parse(response);
			$("#newSmallItem").val(resp.item);
			$("#smallID").val(resp.id);
		});
	}
	else{
		$("#newSmallItem").val("");
		$("#smallID").val("");
	}
	
	$.get("/sales/samples", {"id":sampleID.split('_')[1], "staticTable":"true"}, function(response) {
		var resp = JSON.parse(response);
		$("#sampleAction").html("<h4>Edit existing samples</h4>");
		$("#newLargeItem").val(resp.item);
		$("#largeID").val(resp.id);
	});
	$('html, body').animate({scrollTop:$('#scrollPosition').position().top}, 'slow');
}

//deleteClicked - user selected to delete a specific record (one at a time)
function deleteClicked(event){
	if (confirm('Are you sure you want to delete this record?')) {
		var sample_id = event.target.id.split("_")[1];
		$.ajax({
			type: 'put',
			url: '/sales/samples',
			data: {
				id : sample_id,
				item : "",
				is_small_box : "",
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