from operator import itemgetter
import json

'''
This class holds data that is associated with a HostSite
it is used for basic error protection.
The front end will call the HostSite controller which will
create a HosteSite object and then the controller will call the
database with the values in the object
'''
class HostSite():
	'''Basic no aregument constructor. Sets all values to None'''
	def __init__(self):
		self.id = None
		self.name = None
		self.address = None
		self.city = None
		self.province = None
		self.postalCode = None
		self.phone = None
		self.email = None
		self.hoursOfOperation = {}

	'''This constructor creates a new HostSite and assigns data to the proper variables.'''
	def __init__(self, name, address, city, province, postalCode, hoursOfOperation, phone, email):
		
		values = [None, '']

		self.id = None
		
		#basic error checking is done. If a parameter is an empty string or None it is set to a default vaule

		if name in values:
			self.name = None
		else:
			self.name = name

		if address in values:
			self.address = None
		else:
			self.address = address

		if city in values:
			self.city = None
		else:
			self.city = city

		if province in values:
			self.province = None
		else:
			self.province = province

		if postalCode in values:
			self.postalCode = None
		else:
			self.postalCode = postalCode

		if hoursOfOperation in values:
			self.hoursOfOperation = {"monday":"","tuesday":"","wednesday":"","thursday":"","friday":"","saturday":"","sunday":""}
		else:
			self.hoursOfOperation = {}
			hrs = json.loads(hoursOfOperation)
			self.hoursOfOperation['monday'] = hrs.get('monday',"")
			self.hoursOfOperation['tuesday'] = hrs.get('tuesday',"")
			self.hoursOfOperation['wednesday'] = hrs.get('wednesday',"")
			self.hoursOfOperation['thursday'] = hrs.get('thursday',"")
			self.hoursOfOperation['friday'] = hrs.get('friday',"")
			self.hoursOfOperation['saturday'] = hrs.get('saturday',"")
			self.hoursOfOperation['sunday'] = hrs.get('sunday',"")

		if phone in values:
			self.phone = None
		else:
			self.phone = phone
			
		if email in values:
			self.email = None
		else:
			self.email = email

	''' 
	This is a static method that is used to create a table for the front end
	It is called from the HostSite controller. It sends back HTML.
	HS is a list of dictionaries. Each dictionary contains all the information
	about a HosteSite
	'''
	@staticmethod
	def toTable(hs, isStaticTable):
		# roles = {1:"Administrator", 2:"Coordinator", 3:"Volunteer", 4:"Client"}
		#Here the basic form the table is created
		tableStr = ""
		if isStaticTable == False:
			tableStr = "<div class=\"input-group\" style=\"padding-top: 0;margin-bottom: 5px; margin-top: 0; padding-left: 0\"><span class=\"input-group-addon\">Filter</span><input id=\"filterbox\" type=\"text\" class=\"form-control\" placeholder=\"Type here to filter the table (by sites, dates, names, etc.)\"></div>"
		
		tableStr += "<table class=\"table "
		if isStaticTable == False:
			tableStr += "table-hover"
		tableStr += "\" id=\"hsTable\" style=\"background-color:white;cursor: pointer; cursor: hand; \"><thread><tr id=\"info\"><th>Name</th><th>Phone</th><th>Hours</th><th>Address</th></tr></thread><tbody"
		
		if isStaticTable == False:
			tableStr += " class=\"searchable\">"
		else:
			tableStr += ">"
		
		#This for loop loops through the list of dictionaries and selects certain values to add to the table
		for site in hs:
			tableStr += "<tr id=\"" + str(site.get('id')) + "\" style=\"cursor:pointer;\">"
			tableStr += "<td>" + str(site.get('name')) +"</td>"
			tableStr += "<td>" + str(site.get('phone_number')) +"</td>"
			tableStr += "<td>"
			tableStr += "<ul><li>Monday: " + str(site.get('hours_of_operation').get('monday','')) + "</li>"
			tableStr += "<li>Tuesday: " + str(site.get('hours_of_operation').get('tuesday','')) + "</li>"
			tableStr += "<li>Wednesday: " + str(site.get('hours_of_operation').get('wednesday','')) + "</li>"
			tableStr += "<li>Thursday: " + str(site.get('hours_of_operation').get('thursday','')) + "</li>"
			tableStr += "<li>Friday: " + str(site.get('hours_of_operation').get('friday','')) + "</li>"
			tableStr += "<li>Saturday: " + str(site.get('hours_of_operation').get('saturday','')) + "</li>"
			tableStr += "<li>Sunday: " + str(site.get('hours_of_operation').get('sunday','')) + "</li></ul></td>"
			tableStr += "<td>" + str(site.get('address')) + ", " + str(site.get('city')) + ", " + str(site.get('province')) + ", " + str(site.get('postal_code')) + "</td>"
			if (isStaticTable == False):
				tableStr += "<td><button id=\"delete_" + str(site.get('id')) + "\" type=\"button\" class=\"btn btn-danger\" onclick=\"deleteClicked(event);\">Delete</button></td>"
			tableStr += "</tr>"
			

		tableStr += "</tbody></table>"
		return tableStr