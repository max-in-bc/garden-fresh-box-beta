//setupFilter - add key bindings to filter/search box, and associate .searchable tag with index
//	*Note that much of this is derived from a snippet I found on stackexchange
function setupFilter(){

    (function ($) { //derived from stackexchange help http://goo.gl/weZPrJ

        $('#filterbox').keyup(function () {

            var rex = new RegExp($(this).val(), 'i');
            $('.searchable tr').hide();
            $('.searchable tr').filter(function () {
                return rex.test($(this).text());
            }).show();

        })

    }(jQuery));
}

//getCurrentDate - returns date in a site-standard format
function getCurrentDate(){
	var today = new Date();
	var dd = today.getDate();
	var mm = today.getMonth()+1; //January is 0!
	var yyyy = today.getFullYear();
	
	if(dd<10) {
	    dd='0'+dd
	} 
	
	if(mm<10) {
	    mm='0'+mm
		} 
	
//	today = mm+'/'+dd+'/'+yyyy;
	today = yyyy+'-'+mm+'-'+dd;
	return today;
}

//addRowHandlers - generic function to add click handlers for each row of tables that can be edited/sorted
//	element - is the table element to add the handlers to [required]
//	custom_sort_function - is a pointer to a sort function defined custom for this table
//	custom_load_function - is a pointer to a function defined to load selected rows data to form
function addRowHandlers(element, custom_sort_function, custom_load_function) {
	var table = document.getElementById(element);
	var rows = table.getElementsByTagName("tr");

	if (custom_sort_function != null){
		for (i = 0; i < rows[0].cells.length; i++) {
			var topRow = rows[0].cells
			var currentCol = rows[0].cells[i]
			var createClickHandler = function(column) {
				return function() {
					custom_sort_function(column.innerHTML);
				};
			};
			currentCol.onclick = createClickHandler(currentCol);
		}
	}
	if (custom_load_function != null){
		for (i = 1; i < rows.length; i++) {
			var currentRow = table.rows[i];
			var createClickHandler = function(row) {
				return function() {
					custom_load_function(row.id);
				};
			};
			currentRow.onclick = createClickHandler(currentRow);
		}
	}
}
