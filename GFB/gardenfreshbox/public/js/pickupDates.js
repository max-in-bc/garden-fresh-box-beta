//on page load:
//	update table with list of already created dates
$(window).load(function(){
	$.get('/sales/dates',  {'dateID':'*', "staticTable":"true"}, function(response) {
		$("#list").html(response);
		addRowHandlers("datesTable", null, load_date);
	});
	$("#submit").click(manageDates);
});

//manageDates - if new date then add to database, if existing date then change that date in backend
function manageDates(){
	if($("#hsAction").html().indexOf('Edit existing dates</h4>') > -1){
		//this is an edit
		$.ajax({
			type: 'put',
			url: '/sales/dates',
			data: {
				dateID : $("#dateID").val(),
				orderDate : $("#newOrderDate").val(),
				pickupDate : $("#newPickupDate").val(),
			},
			complete: function(response) {
				if (response.success == "false"){
					alert(response.message);
				} else {
					alert("Date updated successfully")
					location.reload();
				}
			}
		});
	} else {
		//this is an add
		$.ajax({
			type: 'put',
			url: '/sales/dates',
			data: {
				dateID : "",
				orderDate : $("#newOrderDate").val(),
				pickupDate : $("#newPickupDate").val(),
			},
			complete: function(response) {
				if (response.success == "false"){
					alert(response.message);
				} else {
					alert("Date added successfully")
					location.reload();
				}
			}
		});
	}
}

//load_date - user has selected a date from existing list, so update that date to the top form
function load_date(dateID){
	$("#list").removeClass("active");
	$("#" + dateID).addClass("active");
	$("#" + dateID).siblings().removeClass("active");
	
	
	$.get("/sales/dates", {"dateID":dateID, "staticTable":"true"}, function(response) {
		var resp = JSON.parse(response)
		
		$("#hsAction").html("<h4>Edit existing dates</h4>");
		$("#newOrderDate").val(resp.order_date);
		$("#newPickupDate").val(resp.pickup_date);
		$("#dateID").val(dateID);
	});
	$('html, body').animate({scrollTop:$('#scrollPosition').position().top}, 'slow');
}

//deleteClicked - user selected to delete a date, confirm and delete
function deleteClicked(event){
	if (confirm('Are you sure you want to delete this record?')) {
		var date_id = event.target.id.split("_")[1];
		$.ajax({
			type: 'put',
			url: '/sales/dates',
			data: {
				dateID : date_id,
				orderDate : "",
				pickupDate :"",
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