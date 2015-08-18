import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from ast import literal_eval
from gardenfreshbox.lib.base import BaseController, render
from gardenfreshbox.model.cookie import Cookie
from gardenfreshbox.model.user import User
from gardenfreshbox.model.GFBDatabaseController import GFBDatabaseController as DB

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
				users = db.getUsers()
				return User.toTable(users)
			else:
				user = db.getUser(email)
				return json.dumps(user)

		elif (request.method == "PUT"):
			email = request.params['email']
			if(db.userExists(email)):
				# If the user already exists, update them
				user = User(request.params['email'], request.params['password'], request.params['first_name'], request.params['last_name'], request.params['role'], request.params['phone_number'])
# 				user.new_email = request.params['new_email']
				
				success = db.updateUserModel(user)
				if success:
					return self.trueString
				else :
					return "{\"success\":\"false\", \"message\":\"Unable to update user. Ensure email address is correct.\"}"
			else:
				# Add new user
				user = User(request.params['email'], request.params['password'], request.params['first_name'], request.params['last_name'], request.params['role'], request.params['phone_number'])
				success = db.addUserModel(user)
				if success:
					return self.trueString
				else:
					return "{\"success\":\"false\", \"message\":\"Unable to add user.\"}"

		elif (request.method == "DELETE"):
			return "{\"success\":\"false\", \"message\":\"Unimplemented method\"}"

		else:
			return "{\"success\":\"false\",\"message\":\"Bad request method\"}"

	'''
	   This function delete's the users cookie. Without a cookie, the user is not logged in.
	   GET request
	'''
	def logout(self):
		if(request.cookies.get("FCS_GFB_Cookie") != None):
			response.delete_cookie("FCS_GFB_Cookie")
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
				cookie = Cookie(user.get('first_name'), user.get('email'), user.get('fk_credentials_id'), user.get('fk_hostsite_id'))
				response.set_cookie("FCS_GFB_Cookie", cookie.encryptCookie(), max_age=180*24*3600)
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
		cookie = request.cookies.get("FCS_GFB_Cookie")	
		if(cookie == None):
			return ''
		else:
			decode = Cookie.decryptCookie(cookie)
			return json.dumps(decode)