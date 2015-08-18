from operator import itemgetter
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
		self.hostSites = []
		self.newEmail = None

	'''This constructor creates a new User and assigns data to the proper variables.'''
	def __init__(self, email, password, firstName, lastName, credentialsIdFK, phoneNumber):
		
		values = [None, ''] 

		self.hostSites = None
		self.newEmail = None

		#basic error checking is done. If a parameter is an empty string or None it is set to a default vaule

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
		roles = {1:"Site Admin", 2:"GFB Admin", 3:"Host Site Coordinator", 4:"Client"}
		tableStr = "<table class=\"table table-hover\" id=\"usersTable\" style=\"background-color:white;\"><thead><tr id=\"info\"><th>First Name</th><th>Last Name</th><th>Phone</th><th>Email</th><th>Role</th></tr></thread><tbody>"
		
		#This for loop loops through the list of dictionaries and selects certain values to add to the table

		for user in users:
			tableStr += "<tr id=\"" + str(user.get('id')) + "\" style=\"cursor:pointer;\">"
			tableStr += "<td>" + str(user.get('first_name')) +"</td>"
			tableStr += "<td>" + str(user.get('last_name')) +"</td>"
			tableStr += "<td>" + str(user.get('phone_number')) +"</td>"
			tableStr += "<td>" + str(user.get('email')) + "</td>"
			tableStr += "<td>" + str(roles.get(user.get('fk_credentials'),'')) + "</td></tr>"

		tableStr += "</tbody></table>"
		return tableStr