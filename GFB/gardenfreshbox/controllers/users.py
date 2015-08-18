import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from ast import literal_eval
from gardenfreshbox.lib.base import BaseController, render
from gardenfreshbox.model.cookie import Cookie
from gardenfreshbox.model.user import User
from gardenfreshbox.model.GFBDatabaseController import GFBDatabaseController as DB
import os

import json
log = logging.getLogger(__name__)

class UsersController(BaseController):

	trueString = "{\"success\" : \"true\"}"

	'''
	   This funciton manipulates users
	   GET and PUT requests
	'''
	def user(self):
		db = DB()

		# for all users send email : *
		# otherwise user with email will be returned
		if (request.method == "GET"):
			
			email = request.params['email']
			if email == '*':
				users = db.getUsers(request.params['sortid'])
				return User.toTable(users)
			else:
				try:
					user = db.getUser(email)
					return json.dumps(user)
				except:
					return "free"

		elif (request.method == "PUT"):
			email = request.params['email']
			if(db.userExists(email)):
				# If the user already exists, update them
				user = User(request.params['email'], request.params['password'], request.params['first_name'], request.params['last_name'], request.params['role'], request.params['phone_number'], request.params['host_site'])
				success = db.updateUserModel(user, request.params['new_email'])
				if success:
					return self.trueString
				else :
					return "{\"success\":\"false\", \"message\":\"Unable to update user. Ensure email address is correct.\"}"
			
			elif (request.params['email'] != ""):
				# Add new user
				user = User(request.params['email'], request.params['password'], request.params['first_name'], request.params['last_name'], request.params['role'], request.params['phone_number'], request.params['host_site'])
				success = db.addUserModel(user)
				if success:
					self.send_signup_email(request.params['email'], request.params['password'], request.params['first_name'], request.params['last_name'], request.params['role'], request.params['phone_number'], request.params['host_site'])
					return self.trueString
				else:
					return "{\"success\":\"false\", \"message\":\"Unable to add user.\"}"
			
			else:
				# Delete request	
				success = db.removeUser(request.params['id'])
				if success:
					return  "{\"success\":\"true\", \"message\":\"Deleted new host site\"}"
				else:
					return "{\"success\":\"fasle\", \"message\":\"Unable to add new host site\"}"

		elif (request.method == "DELETE"):
			return "{\"success\":\"false\", \"message\":\"Unimplemented method\"}"

		else:
			return "{\"success\":\"false\",\"message\":\"Bad request method\"}"

	def send_signup_email(self, email, password, firstName, lastName, role, phone_number, host_site):
		roles = {1:"Site Admin", 2:"GFB Admin", 3:"Host Site Coordinator", 4:"Client"}
		
		db = DB()
		if (role == "3"):
			pickupSiteName = db.getHostSite(host_site)['name']
		roleTitle = roles.get(int(role))
# 		to_send = 'curl -s --user \'api:key-5bc79fc3330ac42bf29e1b2f89bb1209\' \\\
#     https://api.mailgun.net/v2/sandboxf445b5fad6f649ffa60875af1df80dee.mailgun.org/messages \\\
#     -F from=\'Garden Fresh Box <postmaster@sandboxf445b5fad6f649ffa60875af1df80dee.mailgun.org>\' \\\
#     -F to=\'' + firstName +'<' + email +'>\'\\\
#     -F subject=\'Welcome ' + firstName +'!\' \\\
#     -F text=\'Welcome to Garden Fresh Box ' + firstName +'! \n\nYou just joined the Garden Fresh Box program! Thank you for your patronage, please email the sysadmin at admin@gfb.com if you have any questions or concerns about anything on this site. Here are your personal details which may be edited by logging into the Garden Fresh Box site \n\n\
# 		' + firstName +' ' + lastName + '\n\
# 		Email: ' + email +'\n \
# 		Password: ' + password +'\n \
# 		Role: ' + roleTitle +'\n \
# 		Phone Number: ' + phone_number +'\n '
# 		
# 		if (role == "3"):
# 			to_send = to_send + '\tThe host site you administer: ' + pickupSiteName
# 		
# 		to_send = to_send + '\''
# 		os.system(to_send)
		return

	'''
	   This function delete's the users cookie. Without a cookie, the user is not logged in.
	   GET request
	'''
	def logout(self):
		if(request.cookies.get("GFB_Cookie") != None):
			response.delete_cookie("GFB_Cookie")
		return self.trueString

	'''
	   This function matches provided credentials with creds in the database
	   If a match is made, the user is given a cookie with their system role
	   GET request
	'''
	def auth(self):
		db = DB()
		if (request.method == "GET"):
			# Check if user's email and password are matched
			success = db.authUser(request.params['email'], request.params['password'])

			if(success):
				# Setup the cookie (encrypted) with useful information
				user = db.getUser(request.params['email'])
				cookie = Cookie(user.get('first_name'), user.get('email'), user.get('fk_credentials'), user.get('fk_hostsite_id'))
				response.set_cookie("GFB_Cookie", cookie.encryptCookie(), max_age=180*24*3600)
				return self.trueString
			else:
				return "{\"success\" : \"false\", \"message\" : \"Unable to login: bad username or password\"}"
		else:
			return "{\"success\" : \"false\", \"message\" : \"Bad request.\"}"
		
	def changepassword(self):
		db = DB()
		if (request.method == "PUT"):
			# Check if user's email and password are matched
			success = db.changePassword(request.params['email'], request.params['oldPassword'], request.params['newPassword'])

			if(success):
				return self.trueString
			else:
				return "{\"success\" : \"false\", \"message\" : \"Unable to login: bad username or password\"}"
		else:
			return "{\"success\" : \"false\", \"message\" : \"Bad request.\"}"

	'''
		This method is used by the front end to determine if the user is logged in and get information like name
		GET request
	'''
	def me(self):
		if (request.method == "GET"):
			cookie = request.cookies.get("GFB_Cookie")	
			if(cookie == None):
				return ''
			else:
				decode = Cookie.decryptCookie(cookie)
				return json.dumps(decode)
		else: #open host site
			cookie = request.cookies.get("GFB_Cookie")	
			if(cookie == None):
				return ''
			else:
				encode = {}
				decode = Cookie.decryptCookie(cookie)
				encode['role'] = decode['role']
				encode['user_name'] = decode['user_name']
				encode['email'] = decode['email']
				
				if (request.params['changed'] == 'true'):
					encode['host_site'] = request.params['siteID']
				else:
					encode['host_site'] = ''
					
				cookie = Cookie(encode['user_name'],encode['email'], encode['role'], encode['host_site'])
				response.delete_cookie('GFB_Cookie')
				response.set_cookie("GFB_Cookie", cookie.encryptCookie(), max_age=180*24*3600)
									
				return render('/tools/distOrders.mako')
			