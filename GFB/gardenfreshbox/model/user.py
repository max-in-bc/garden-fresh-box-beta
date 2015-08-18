from operator import itemgetter
from gardenfreshbox.model.GFBDatabaseController import GFBDatabaseController as DB
import json

'''
This class holds data that is associated with a User
It is used for basic error protection and is a go between for the
front end and the database.
The front end will call the User controller which will
create a User object and then the controller will call the
database with the values in the object
'''

class User():
	
	'''No argument constructor that initializes a User object'''
	def __init__(self):
		self.id = None
		self.credentialsIdFK = None
		self.email = None
		self.firstName = None
		self.lastName = None
		self.phoneNumber = None
		self.password = None
		self.hostSite = None
		self.newEmail = None

	'''This constructor creates a new User and assigns data to the proper variables.'''
	def __init__(self, email, password, firstName, lastName, credentialsIdFK, phoneNumber, hostSite):
		
		values = [None, ''] 

		self.newEmail = None

		#basic error checking is done. If a parameter is an empty string or None it is set to a default vaule

		
		if hostSite in values:
			self.hostSite = None
		else:
			self. hostSite = hostSite

		if email in values:
			self.email = None
		else:
			self. email = email

		if password in values:
			self.password = None
		else:
			self.password = password

		if firstName in values:
			self.firstName = None
		else:
			self.firstName = firstName

		if lastName in values:
			self.lastName = None
		else:
			self.lastName = lastName

		if credentialsIdFK in values:
			self.credentialsIdFK = None
		else:
			self.credentialsIdFK = credentialsIdFK

		if phoneNumber in values:
			self.phoneNumber = 0
		else:
			self.phoneNumber = phoneNumber


	''' 
	This is a static method that is used to create a table for the front end
	It is called from the User controller. It sends back HTML.
	users is a list of dictionaries. Each dictionary contains all the information
	about a user.
	'''
	@staticmethod
	def toTable(users):
		db = DB()
		roles = {1:"Site Admin", 2:"GFB Admin", 3:"Host Site Coordinator", 4:"Client"}
		tableStr = "<div class=\"input-group\" style=\"padding-top: 0;margin-bottom: 5px; margin-top: 0; padding-left: 0\"><span class=\"input-group-addon\">Filter</span><input id=\"filterbox\" type=\"text\" class=\"form-control\" placeholder=\"Type here to filter the table (by sites, dates, names, etc.)\"></div>"
		tableStr += "<table class=\"table table-hover\" id=\"usersTable\" style=\"background-color:white;cursor: pointer; cursor: hand; \"><thread><tr id=\"info\"><th>First Name</th><th>Last Name</th><th>Phone</th><th>Email</th><th>Host Site</th><th>Role</th></tr></thread><tbody class=\"searchable\">"
		
			
		#This for loop loops through the list of dictionaries and selects certain values to add to the table
		for user in users:
			hostsite_name = "None";
			if (user.get('fk_credentials') == 1 or user.get('fk_credentials') == 2):
				hostsite_name = "All"
			
			if (user.get('fk_hostsite_id') != None):
				hsInfo = db.getHostSite(user.get('fk_hostsite_id'))
				if (hsInfo != None):
					hostsite_name = hsInfo['name']
			
					
			
			tableStr += "<tr id=\"" + str(user.get('id')) + "\" style=\"cursor:pointer;\">"
			tableStr += "<td>" + str(user.get('first_name')) +"</td>"
			tableStr += "<td>" + str(user.get('last_name')) +"</td>"
			tableStr += "<td>" + str(user.get('phone_number')) +"</td>"
			tableStr += "<td>" + str(user.get('email')) + "</td>"
			tableStr += "<td>" + hostsite_name + "</td>"
			tableStr += "<td>" + str(roles.get(user.get('fk_credentials'),'')) + "</td>"
			tableStr += "<td><button id=\"delete_" + str(user.get('id')) + "\" type=\"button\" class=\"btn btn-danger\" onclick=\"deleteClicked(event);\">Delete</button></td></tr>"
			
		tableStr += "</tbody></table>"
		return tableStr