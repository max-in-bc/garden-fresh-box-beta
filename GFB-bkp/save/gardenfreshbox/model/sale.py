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
	def __init__(self, orderId, creationDate, distributionDate, customerFirstName, customerLastName, customerEmail, customerPhone, emailNotifications, smallQuantity, largeQuantity, donation, donationReceipt, totalPaid, hostsitepickupIdFK, hostsitecreatedIdFK):
		
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
			parts = distributionDate.split('/')
			d = datetime.date(int(parts[2]),int(parts[0]),int(parts[1]))
			self.distributionDate = d

		if creationDate in values:
			self.creationDate = None
		else:
			# mm/dd/yyyy
			parts = creationDate.split('/')
			d = datetime.date(int(parts[2]),int(parts[0]),int(parts[1]))
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

		tableStr = "<table class=\"table\" id=\"donorTable\" style=\"background-color:white;\"><thead><tr id=\"info\"><th>Name</th><th>Phone</th><th>Email</th><th>Reciept</th><th>Amount</th></tr></thread><tbody><tr>"
		
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
		tableStr = "<table class=\"table\" id=\"ordersTable\" style=\"background-color:white;\"><thead><tr id=\"info\"><th>Host Site</th><th>Small Boxes</th><th>Large Boxes</th></tr></thread><tbody><tr>"
	
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
		tableStr = "<table class=\"table\" id=\"custTable\" style=\"background-color:white;\"><thead><tr id=\"info\"><th>Name</th><th>Phone</th><th>Email</th></tr></thread><tbody><tr>"
		
		#This for loop loops through the list of dictionaries and selects certain values to add to the table

		for site in customer:
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
		tableStr = "<table class=\"table\" id=\"usersTable\" style=\"background-color:white;\"><thead><tr id=\"info\"><th>Pickup Site</th><th>Pickup Date</th><th>Customer</th><th>Phone</th><th>Email</th><th>No. Small</th><th>No. Large</th><th>Paid</th><th>Owing</th><th>Donation</th><th>Ordered On</th></tr></thread><tbody>"
		
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
			tableStr += "<td>" + str(owe) +"</td>"
			
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
		tableStr = "<table class=\"table\" id=\"usersTable\" style=\"background-color:white;\"><thead><tr id=\"info\"><th>Pickup Site</th><th>Pickup Date</th><th>Customer</th><th>Phone</th><th>Email</th><th>No. Small</th><th>No. Large</th><th>Paid</th><th>Owing</th><th>Donation</th><th>Ordered On</th></tr></thread><tbody>"
		
		#calls to database is made to get the name of the hostsite
		db = DB()
		hostSite = db.getHostSiteByName(hostSiteName)

		#This for loop loops through the list of dictionaries and selects certain values to add to the table

		for order in orders:
			if str(order.get('hostsitepickup_idFK','')) != str(hostSite.get('id')):
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
			tableStr += "<td>" + str(owe) +"</td>"
			
			tableStr += "<td>" + str(order.get('donation'))
			if str(order.get('donation_receipt')) == "1":
				tableStr += " (Reciept)</td>"
			else:
				tableStr += "</td>"

			tableStr += "<td>" + str(order.get('creation_date')) +"</td>"
			tableStr += "</td></tr>"

		tableStr += "</tbody></table>"
		return tableStr
