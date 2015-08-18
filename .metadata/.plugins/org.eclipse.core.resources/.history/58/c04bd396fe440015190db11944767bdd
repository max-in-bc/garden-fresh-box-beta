import json
from gardenfreshbox.model.GFBDatabaseController import GFBDatabaseController as DB
import datetime

'''
This class holds data that is associated with a Sale
It is used for basic error protection and is a go between for the
front end and the database.
The front end will call the Sales controller which will
create a Sale object and then the controller will call the
database with the values in the object
'''
class Sale():
	'''This constructor creates a new Sale and assigns data to the proper variables.'''
	def __init__(self, orderId, creationDate, distributionDate, customerFirstName, customerLastName, customerEmail, customerPhone, emailNotifications, smallQuantity, largeQuantity, donation, donationReceipt, totalPaid, hostsitepickupIdFK, hostsitecreatedIdFK, customerID):
		
		values = [None,'']

		#basic error checking is done. If a parameter is an empty string or None it is set to a default vaule

		if orderId in values:
			self.orderId = None
		else:
			self.orderId = orderId

		if distributionDate in values:
			self.distributionDate = None
		else:
			# mm/dd/yyyy
			parts = distributionDate.split('-')
			d = datetime.date(int(parts[0]),int(parts[1]),int(parts[2]))
			self.distributionDate = d

		if creationDate in values:
			self.creationDate = None
		else:
			# mm/dd/yyyy
			parts = creationDate.split('-')
			d = datetime.date(int(parts[0]),int(parts[1]),int(parts[2]))
			self.creationDate = d

		if customerFirstName in values:
			self.customerFirstName = None
		else:
			self.customerFirstName = customerFirstName

		if customerLastName in values:
			self.customerLastName = None
		else:
			self.customerLastName = customerLastName

		if customerEmail in values:
			self.customerEmail = ''
		else:
			self.customerEmail = customerEmail

		if customerPhone in values:
			self.customerPhone = ''
		else:
			self.customerPhone = customerPhone

		if emailNotifications in values:
			self.emailNotifications = 0
		else:
			self.emailNotifications = emailNotifications

		if smallQuantity in values:
			self.smallQuantity = 0
		else:
			self.smallQuantity = smallQuantity

		if largeQuantity in values:
			self.largeQuantity = 0
		else:
			self.largeQuantity = largeQuantity

		if donation in values:
			self.donation = 0
		else:
			self.donation = donation

		if donationReceipt in values:
			self.donationReceipt = 0
		else:
			self.donationReceipt = donationReceipt

		if totalPaid in values:
			self.totalPaid = 0
		else:
			self.totalPaid = totalPaid
		
		if customerID in values:
			self.customerID = None
		else:
			self.customerID = customerID
			
		if hostsitepickupIdFK in values:
			self.hostsitepickupIdFK = None
		else:
			self.hostsitepickupIdFK = hostsitepickupIdFK

		if hostsitecreatedIdFK in values:
			self.hostsitecreatedIdFK = None
		elif hostsitecreatedIdFK == "-99":
			# this order was placed online
			db = DB()
			hostSite = db.getHostSiteByName("Online")
			self.hostsitecreatedIdFK = hostSite.get('id')
		else:
			self.hostsitecreatedIdFK = hostsitecreatedIdFK
		
		self.dict = {}

	''' 
	This is a static method that is used to create a table for the front end
	It is called from the Sales controller. It sends back HTML.
	donors is a list of dictionaries. Each dictionary contains all the information
	about a donor.
	This table is in sales because we get a list of Donors from orders(ie sales) that have
	been placed.
	'''
	@staticmethod
	def toTableDonations(donors):
		
		#Here the basic form the table is created

		tableStr = "<div class=\"input-group\" style=\"padding-top: 0;margin-bottom: 5px; margin-top: 0; padding-left: 0\"><span class=\"input-group-addon\">Filter</span><input id=\"filterbox\" type=\"text\" class=\"form-control\" placeholder=\"Type here to filter the table (by sites, dates, names, etc.)\"></div>"
		tableStr += "<table class=\"table\" id=\"donorTable\" style=\"background-color:white;cursor: pointer; cursor: hand; \"><thread><tr id=\"info\"><th>Name</th><th>Phone</th><th>Email</th><th>Reciept</th><th>Amount</th></tr></thread><tbody class=\"searchable\"><tr>"
		
		#This for loop loops through the list of dictionaries and selects certain values to add to the table

		for site in donors:
			tableStr += "<td>" + str(site.get('customer_first_name')) +" "+ str(site.get('customer_last_name')) +"</td>"
			tableStr += "<td>" + str(site.get('customer_phone')) +"</td>"
			tableStr += "<td>" + str(site.get('customer_email')) + "</td>"
			tableStr += "<td>" + str(site.get('donation_receipt')) + "</td>"
			tableStr += "<td>" + str(site.get('donation')) +"</td></tr>"

		tableStr += "</tbody></table>"
		return tableStr

	''' 
	This is a static method that is used to create a table for the front end
	It is called from the Sales controller. It sends back HTML.
	orders is a list of dictionaries. Each dictionary contains all the information
	about a order.
	This method collects all the small and large orders from each HS and
	combinds them in one table.
	This table is in sales because we get a list of orders from orders(ie sales) that have
	been placed.
	'''
	@staticmethod
	def toTableMasterOrderList(orders):
		tableStr = "<div class=\"input-group\" style=\"padding-top: 0;margin-bottom: 5px; margin-top: 0; padding-left: 0\"><span class=\"input-group-addon\">Filter</span><input id=\"filterbox\" type=\"text\" class=\"form-control\" placeholder=\"Type here to filter the table (by sites, dates, names, etc.)\"></div>"
		tableStr += "<table class=\"table\" id=\"ordersTable\" style=\"background-color:white;cursor: pointer; cursor: hand; \"><thread><tr id=\"info\"><th>Host Site</th><th>Small Boxes</th><th>Large Boxes</th></tr></thread><tbody class=\"searchable\">"
	
		#A database object is created
		db = DB()
		
		'''
		The first loop is used to scan the list of orders and find all the orders from each hostsite
		it creates a new dictionary with the total number of boxes in it.
		'''
		ords = {}
		ids = []

		for site in orders:
			currId = site.get('hostsitepickup_idFK')
			
			if currId in ids:
				ords[currId]['small_quantity'] += int(site.get('small_quantity'))
				ords[currId]['large_quantity'] += int(site.get('large_quantity'))
			else:
				ids.append(currId)
				ords[currId] = {}
				ords[currId]['small_quantity'] = int(site.get('small_quantity'))
				ords[currId]['large_quantity'] = int(site.get('large_quantity'))

		#This for loop goes through the dictionary and selects values to be added to the table
		
		for key in ords.keys():
			site = ords.get(key)
			dic = db.getHostSite(key)
			if dic == None:
				continue
			tableStr += "<tr id=\"" + str(key) + "\">"
			
			tableStr += "<td>" + str(dic['name']) +"</td>"
			tableStr += "<td>" + str(site.get('small_quantity')) +"</td>"
			tableStr += "<td>" + str(site.get('large_quantity')) +"</td></tr>"

		tableStr += "</tbody></table>"
		return tableStr

	''' 
	This is a static method that is used to create a table for the front end
	It is called from the Sales controller. It sends back HTML.
	customer is a list of dictionaries. Each dictionary contains all the information
	about a customer.
	This table is in sales because we get a list of customer from orders(ie sales) that have
	been placed.
	'''
	@staticmethod
	def toTableMasterCustomerList(customer):
		tableStr = "<div class=\"input-group\" style=\"padding-top: 0;margin-bottom: 5px; margin-top: 0; padding-left: 0\"><span class=\"input-group-addon\">Filter</span><input id=\"filterbox\" type=\"text\" class=\"form-control\" placeholder=\"Type here to filter the table (by sites, dates, names, etc.)\"></div>"
		tableStr += "<table class=\"table table-hover\" id=\"custTable\" style=\"background-color:white;cursor: pointer; cursor: hand; \"><thread><tr id=\"info\"><th>Name</th><th>Phone</th><th>Email</th></tr></thread><tbody class=\"searchable\">"
		
		#This for loop loops through the list of dictionaries and selects certain values to add to the table

		for site in customer:
			tableStr += "<tr class=\"" + str(site.get('customer_id')) + "\" id=\"" + str(site.get('customer_email')) + "\">"
			tableStr += "<td>" +  str(site.get('customer_first_name')) +" "+ str(site.get('customer_last_name')) +"</td>"
			tableStr += "<td>" + str(site.get('customer_phone')) +"</td>"
			tableStr += "<td>" + str(site.get('customer_email')) +"</td></tr>"

		tableStr += "</tbody></table>"
		return tableStr

	''' 
	This is a static method that is used to create a table for the front end
	It is called from the Sales controller. It sends back HTML.
	orders is a list of dictionaries. Each dictionary contains all the information
	about a order.
	hostSiteName is the id of the HostSite
	This table is in sales because we get a list of orders from orders(ie sales) that have
	been placed.
	'''
	@staticmethod	
	def toCashSaleList(orders, hostSiteName):
		tableStr = "<table class=\"table\" id=\"usersTable\" style=\"background-color:white;cursor: pointer; cursor: hand; \"><thread><tr id=\"info\"><th>Pickup Site</th><th>Pickup Date</th><th>Customer</th><th>Phone</th><th>Email</th><th>No. Small</th><th>No. Large</th><th>Paid</th><th>Donation</th><th>Ordered On</th></tr></thread><tbody>"
		
		#calls to database is made to get the name of the hostsite
		
		db = DB()
		hostSite = db.getHostSiteByName(hostSiteName)

		#This for loop loops through the list of dictionaries and selects certain values to add to the table

		for order in orders:
			if str(order.get('hostsitecreated_idFK','')) != str(hostSite.get('id')):
				continue;

			tableStr += "<tr id=\"" + str(order.get('id')) + "\">"
			tableStr += "<td>" + hostSiteName +"</td>"
			
			tableStr += "<td>" + str(order.get('distribution_date')) +"</td>"
			tableStr += "<td>" + str(order.get('customer_first_name')) + " " + str(order.get('customer_last_name')) +"</td>"
			tableStr += "<td>" + str(order.get('customer_phone')) +"</td>"
			tableStr += "<td>" + str(order.get('customer_email'))
			if str(order.get('email_notifications')) == "1":
				tableStr += " (Notifications)</td>"
			else:
				tableStr += "</td>"
			
			tableStr += "<td>" + str(order.get('small_quantity')) +"</td>"
			tableStr += "<td>" + str(order.get('large_quantity')) +"</td>"
			tableStr += "<td>" + str(order.get('total_paid')) +"</td>"
			
			cost = 20.0 * float(order.get('large_quantity', 0)) + 15.0 * float(order.get('small_quantity', 0))
			owe = cost - float(order.get('total_paid', 0.00))
			
			tableStr += "<td>" + str(order.get('donation'))
			if str(order.get('donation_receipt')) == "1":
				tableStr += " (Reciept)</td>"
			else:
				tableStr += "</td>"

			tableStr += "<td>" + str(order.get('creation_date')) +"</td>"
			tableStr += "</td></tr>"

		tableStr += "</tbody></table>"
		return tableStr

	
	''' 
	This is a static method that is used to create a table for the front end
	It is called from the Sales controller. It sends back HTML.
	orders is a list of dictionaries. Each dictionary contains all the information
	about a order.
	hostSiteName is the id of the HostSite
	This function creates a table for orders to distribute
	This table is in sales because we get a list of orders from orders(ie sales) that have
	been placed.
	'''
	@staticmethod	
	def toDistList(orders, hostSiteName):
		tableStr = "<div class=\"input-group\" style=\"padding-top: 0;margin-bottom: 5px; margin-top: 0; padding-left: 0\"><span class=\"input-group-addon\">Filter</span><input id=\"filterbox\" type=\"text\" class=\"form-control\" placeholder=\"Type here to filter the table (by sites, dates, names, etc.)\"></div>"
		tableStr += "<table class=\"table\" id=\"usersTable\" style=\"background-color:white;cursor: pointer; cursor: hand; \"><thread><tr id=\"info\"><th>Pickup Site</th><th>Pickup Date</th><th>Customer</th><th>Phone</th><th>Email</th><th>No. Small</th><th>No. Large</th><th>Paid</th><th>Ordered On</th><th></th></tr></thread><tbody class=\"searchable\">"
		
		#calls to database is made to get the name of the hostsite
		db = DB()
		hostSite = db.getHostSiteByName(hostSiteName)

		#This for loop loops through the list of dictionaries and selects certain values to add to the table

		for order in orders:
			is_not_overdue = False
			d_date = datetime.datetime.strptime(order.get('distribution_date'), '%Y-%m-%d') - datetime.timedelta(days=12)
			current_date = datetime.datetime.today()
			
			
			if (current_date < d_date):
				is_not_overdue = True
				
# 			if str(order.get('hostsitepickup_idFK','')) != str(hostSite.get('id')):
# 				continue;

			tableStr += "<tr id=\"" + str(order.get('id')) + "\">"
			tableStr += "<td>" + hostSiteName +"</td>"
			
			tableStr += "<td>" + str(order.get('distribution_date')) +"</td>"
			tableStr += "<td>" + str(order.get('customer_first_name')) + " " + str(order.get('customer_last_name')) +"</td>"
			tableStr += "<td>" + str(order.get('customer_phone')) +"</td>"
			tableStr += "<td>" + str(order.get('customer_email'))
			if str(order.get('email_notifications')) == "1":
				tableStr += " (Notifications)</td>"
			else:
				tableStr += "</td>"
			
			tableStr += "<td>" + str(order.get('small_quantity')) +"</td>"
			tableStr += "<td>" + str(order.get('large_quantity')) +"</td>"
			if float(order.get('total_paid')) > 0.0:
				isPaid = "Paid"
				buttonType = "success"
			else:
				isPaid = "Unpaid"
				if (is_not_overdue):
					buttonType = "primary"
				else:
					buttonType = "warning"
			tableStr += "<td><button id=\"paid_" + str(order.get('id')) + "\" type=\"button\" class=\"label label-"+ buttonType + "\">" + isPaid +"</td>"
			
			cost = 20.0 * float(order.get('large_quantity', 0)) + 15.0 * float(order.get('small_quantity', 0))
			owe = cost - float(order.get('total_paid', 0.00))
# 			tableStr += "<td>" + str(owe) +"</td>"
# 			
# 			tableStr += "<td>" + str(order.get('donation'))
			if str(order.get('donation_receipt')) == "1":
				tableStr += " (Reciept)</td>"
			else:
				tableStr += "</td>"

			tableStr += "<td>" + str(order.get('creation_date')) +"</td>"
			tableStr += "</td>"
			
			tableStr += "<td><button id=\"delete_" + str(order.get('id')) + "\" type=\"button\" class=\"btn btn-danger\" onclick=\"deleteClicked(event);\">Delete</button></td>"
		
			tableStr += "</tr>"

		tableStr += "</tbody></table>"
		return tableStr
	
	''' 
	This is a static method that is used to create a table for the front end
	It is called from the Sales controller. It sends back HTML.
	orders is a list of dictionaries. Each dictionary contains all the information
	about a order.
	This function creates a table for orders of this user
	This table is in sales because we get a list of orders from orders(ie sales) that have
	been placed.
	'''
	@staticmethod	
	def toUserSaleList(orders):
		tableStr = "<div class=\"input-group\" style=\"padding-top: 0;margin-bottom: 5px; margin-top: 0; padding-left: 0\"><span class=\"input-group-addon\">Filter</span><input id=\"filterbox\" type=\"text\" class=\"form-control\" placeholder=\"Type here to filter the table (by sites, dates, names, etc.)\"></div>"
		tableStr += "<table class=\"table table-hover\" id=\"ordersTable\" style=\"background-color:white;cursor: pointer; cursor: hand; \"><thread><tr id=\"info\"><th>Pickup Site</th><th>Pickup Date</th><th>Customer</th><th>Phone</th><th>Email</th><th>No. Small</th><th>No. Large</th><th>Paid</th><th>Ordered On</th></tr></thread><tbody class=\"searchable\">"
		
		#calls to database is made to get the name of the hostsite
		db = DB()
		#This for loop loops through the list of dictionaries and selects certain values to add to the table

		
		for order in orders:
			is_not_overdue = False
			d_date = datetime.datetime.strptime(order.get('distribution_date'), '%Y-%m-%d') - datetime.timedelta(days=12)
			current_date = datetime.datetime.today()
			
			
			if (current_date < d_date):
				is_not_overdue = True
				
			ordered_from_name = "None";
			if (order.get('hostsitepickup_idFK') != None):
				hsInfo = db.getHostSite(order.get('hostsitepickup_idFK'))
				if (hsInfo != None):
					ordered_from_name = hsInfo['name']
					
			tableStr += "<tr id=\"" + str(order.get('id')) + "\">"
			
			tableStr += "<td>" + ordered_from_name +"</td>"
			tableStr += "<td>" + str(order.get('distribution_date')) +"</td>"
			tableStr += "<td>" + str(order.get('customer_first_name')) + " " + str(order.get('customer_last_name')) +"</td>"
			tableStr += "<td>" + str(order.get('customer_phone')) +"</td>"
			tableStr += "<td>" + str(order.get('customer_email'))
			if str(order.get('email_notifications')) == "1":
				tableStr += " (Notifications)</td>"
			else:
				tableStr += "</td>"
			
			tableStr += "<td>" + str(order.get('small_quantity')) +"</td>"
			tableStr += "<td>" + str(order.get('large_quantity')) +"</td>"
			if float(order.get('total_paid')) > 0.0:
				isPaid = "Paid"
				buttonType = "success"
			else:
				isPaid = "Unpaid"
				if (is_not_overdue):
					buttonType = "primary"
				else:
					buttonType = "warning"
			tableStr += "<td><button id=\"paid_" + str(order.get('id')) + "\" type=\"button\" class=\"label label-"+ buttonType + "\">" + isPaid +"</td>"
			
			cost = 20.0 * float(order.get('large_quantity', 0)) + 15.0 * float(order.get('small_quantity', 0))
			owe = cost - float(order.get('total_paid', 0.00))

			
			tableStr += "<td>" + str(order.get('creation_date')) +"</td>"
			if (is_not_overdue and order.get('total_paid') == "0.00"):
				tableStr += "<td><button id=\"delete_" + str(order.get('id')) + "\" type=\"button\" class=\"btn btn-danger\" onclick=\"deleteClicked(event);\">Delete</button></td>"
			
			tableStr += "</tr>"

		tableStr += "</tbody></table>"
		return tableStr
	
	''' 
	This is a static method that is used to create a table for the front end
	It is called from the Sales controller. It sends back HTML.
	orders is a list of dictionaries. Each dictionary contains all the information
	about a order.
	This function creates a table for orders of this user
	This table is in sales because we get a list of orders from orders(ie sales) that have
	been placed.
	'''
	@staticmethod	
	def toUserDonationList(orders):
		tableStr = "<div class=\"input-group\" style=\"padding-top: 0;margin-bottom: 5px; margin-top: 0; padding-left: 0\"><span class=\"input-group-addon\">Filter</span><input id=\"filterbox\" type=\"text\" class=\"form-control\" placeholder=\"Type here to filter the table (by sites, dates, names, etc.)\"></div>"
		tableStr += "<table class=\"table\" id=\"ordersTable\" style=\"background-color:white;\"><thread><tr id=\"info\"><th>Customer</th><th>Phone</th><th>Email</th><th>Donation</th><th>Donated On</th></tr></thread><tbody class=\"searchable\">"
		
		#calls to database is made to get the name of the hostsite
		db = DB()
		

		#This for loop loops through the list of dictionaries and selects certain values to add to the table

		for order in orders:
			tableStr += "<tr id=\"" + str(order.get('id')) + "\">"
			
			tableStr += "<td>" + str(order.get('customer_first_name')) + " " + str(order.get('customer_last_name')) +"</td>"
			tableStr += "<td>" + str(order.get('customer_phone')) +"</td>"
			tableStr += "<td>" + str(order.get('customer_email'))
			if str(order.get('email_notifications')) == "1":
				tableStr += " (Notifications)</td>"
			else:
				tableStr += "</td>"
			
			
			tableStr += "<td>" + str(order.get('donation'))
			if str(order.get('donation_receipt')) == "1":
				tableStr += " (Reciept)</td>"
			else:
				tableStr += "</td>"

			tableStr += "<td>" + str(order.get('creation_date')) +"</td>"
			tableStr += "</td></tr>"

		tableStr += "</tbody></table>"
		return tableStr
	
	
	''' 
	This is a static method that is used to create a table for the front end
	It is called from the Sales controller. It sends back HTML.
	dates is a list of dictionaries. Each dictionary contains all the information
	about pickup and delivery dates.
	This table is in sales because we get a list of orders from orders(ie sales) 
	
	isStatic is a boolean key that will differentiate if this list will be updated from this page or not
	'''
	
	@staticmethod	
	def toTableDates(dates, isStatic):
		tableStr = "<table class=\"table table-condensed\" "
		if (isStatic== "true"):
			tableStr = "<table class=\"table table-hover\" "
			
		tableStr += "id=\"datesTable\" style=\"background-color:white;max-width:50%;\"><thread><tr id=\"pickup_dates\">"
		if (isStatic== "true"):
			tableStr += "<th>Date ID</th>"
		tableStr += "<th>Pickup Due</th><th>Order Due</th></tr></thread><tbody>"
		
		#calls to database is made to get the name of the hostsite
		db = DB()

		#This for loop loops through the list of dictionaries and selects certain values to add to the table
		for date in dates:
			
			tableStr += "<tr id=\"" + str(date.get('id')) + "\">"
			if (isStatic== "true"):
				tableStr += "<td id=\"date_" +  str(date.get('id')) + "\">" + str(date.get('id')) +"</td>"
			tableStr += "<td>" + str(date.get('pickup_date')) +"</td>"
			tableStr += "<td>" + str(date.get('order_date')) +"</td>"
			if (isStatic== "true"):
				tableStr += "<td><button id=\"delete_" + str(date.get('id')) + "\" type=\"button\" class=\"btn btn-danger\" onclick=\"deleteClicked(event);\">Delete</button></td></tr>"
			tableStr += "</tr>"

		tableStr += "</tbody></table>"
		return tableStr

	def paypalIPN(self):
		return 1



	''' 
	This is a static method that is used to create a table for the front end
	It is called from the Sales controller. It sends back HTML.
	dates is a list of dictionaries. Each dictionary contains all the information
	about pickup and delivery dates.
	This table is in sales because we get a list of orders from orders(ie sales) 
	
	isStatic is a boolean key that will differentiate if this list will be updated from this page or not
	'''
	
	@staticmethod	
	def toTableSampleBoxes(smallitems,largeitems, isStatic):
		tableStr = "<table class=\"table table-condensed\" "
		if (isStatic== "true"):
			tableStr = "<table class=\"table table-hover\" "
			
		tableStr += "id=\"samplesTable\" style=\"background-color:white;cursor: pointer; cursor: hand; \"><thread><tr id=\"sample_items\">"
		if (isStatic== "true"):
			tableStr += "<th>Large Box ($20)</th><th></th><th>Small Box ($15)</th><th></th></tr></thread><tbody>"
		else:
			tableStr += "<th>Large Box ($20)</th><th>Small Box ($15)</th></tr></thread><tbody>"
		

		#This for loop loops through the list of dictionaries and selects certain values to add to the table
		for i in range(len(largeitems)):
			
			
			if (len(smallitems) > i):
				tableStr += "<tr id=\"" + str(smallitems[i].get('id')) + "_" +  str(largeitems[i].get('id')) + "\">"
			else:
				tableStr += "<tr id=\"" + "?_" +  str(largeitems[i].get('id')) + "\">"
			
			tableStr += "<td>" + str(largeitems[i].get('item'))
			tableStr += "</td>"
			if (isStatic== "true"):
				tableStr += "<td><button style=\"float:right; \" id=\"deletelarge_" + str(largeitems[i].get('id')) + "\" type=\"button\" class=\"btn btn-danger\" onclick=\"deleteClicked(event);\">Delete</button></td>"
			
			if (len(smallitems) > i):
				tableStr += "<td>" + str(smallitems[i].get('item')) +"</td>"
				if (isStatic== "true"):
					tableStr += "<td><button style=\"float:right; \" id=\"deletesmall_" + str(smallitems[i].get('id')) + "\" type=\"button\" class=\"btn btn-danger\" onclick=\"deleteClicked(event);\">Delete</button></td>"
			
			
			tableStr += "</tr>"

		tableStr += "</tbody></table>"
		return tableStr