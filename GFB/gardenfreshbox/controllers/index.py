import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from ast import literal_eval
from gardenfreshbox.lib.base import BaseController, render
from gardenfreshbox.model.cookie import Cookie

log = logging.getLogger(__name__)

class IndexController(BaseController):

	'''
	   Returns the homepage
	'''
	def index(self):
		return render('/index.mako');
	
	'''
	   Returns the contact page
	'''
	def contact(self):
		return render('/contact/contact.mako')

	'''
	   Returns the info page
	'''
	def info(self):
		return render('info/info.mako')

	'''
	   Returns the cash sales page
	   If user does not have access, throws 404
	'''
	def cashsales(self):
		cookie = request.cookies.get("GFB_Cookie")
		if(cookie == None):
			response.status_int = 404
			return
		else:
			creds = Cookie.decryptCookie(cookie)
			if (creds.get('role') == '1') or (creds.get('role') == '2') or (creds.get('role') == '3'):
				return render('/tools/cashSales.mako')
			else:
				response.status_int = 404
				return

	'''
	   Returns the donation page
	'''
	def donate(self):
		return render('/donate/donate.mako')

	'''
	   Returns the login page
	'''
	def login(self):
		return render('/login.mako')

	'''
	   Returns the purchase page
	'''
	def buy(self):
		return render("/shop/newOrder.mako");

	'''
	   Returns the administrator dashboard
	   If user does not have access, throws 404
	'''
	def dashboard(self):
		cookie = request.cookies.get("GFB_Cookie")
		if(cookie == None):
			response.status_int = 404
			return
		else:
			creds = Cookie.decryptCookie(cookie)
			return render('/tools/dashboard.mako')
	
	'''
	   Returns all the logged in users donations
	'''
	def yourorders(self):
		return render('tools/yourOrders.mako')
	
	'''
	   Returns all the logged in users donations
	'''
	def yourdonations(self):
		return render('tools/yourDonations.mako')

	'''
	   Returns the manage host sites page
	   If user does not have access, throws 404
	'''
	def manageHS(self):
		cookie = request.cookies.get("GFB_Cookie")
		if(cookie == None):
			response.status_int = 404
			return
		else:
			creds = Cookie.decryptCookie(cookie)
			if(creds.get('role') == '3' or creds.get('role') == '2' or creds.get('role') == '1'):
				return render("/tools/manageHS.mako");
			else:
				response.status_int = 404
				return

	'''
	   Returns the manage accounts sites page
	   If user does not have access, throws 404
	'''
	def manageAccounts(self):
		cookie = request.cookies.get("GFB_Cookie")
		if(cookie == None):
			response.status_int = 404
			return
		else:
			creds = Cookie.decryptCookie(cookie)

			if (creds.get('role') == '2') or (creds.get('role') == '1'):
				return render('/tools/manageAccounts.mako')
			else:
				response.status_int = 404
				return

	'''
	   Returns the master order list
	   If user does not have access, throws 404
	'''
	def masterOrderList(self):
		#look at cookie
		cookie = request.cookies.get("GFB_Cookie")
		if(cookie == None):
			response.status_int = 404
			return
		else:
			creds = Cookie.decryptCookie(cookie)
			if (creds.get('role') == '2') or (creds.get('role') == '1'):
				return render('/tools/orderList.mako')
			else:
				response.status_int = 404
				return

	'''
	   Returns the master donor list
	   If user does not have access, throws 404
	'''
	def masterDonorList(self):
		#look at cookie
		cookie = request.cookies.get("GFB_Cookie")
		if(cookie == None):
			response.status_int = 404
			return
		else:
			creds = Cookie.decryptCookie(cookie)
			if (creds.get('role') == '2') or (creds.get('role') == '1'):
				return render('/tools/donationsList.mako')
			else:
				response.status_int = 404
				return

	'''
	   Returns the master customer list
	   If user does not have access, throws 404
	'''
	def masterCustList(self):
		#look at cookie
		cookie = request.cookies.get("GFB_Cookie")
		if(cookie == None):
			response.status_int = 404
			return
		else:
			creds = Cookie.decryptCookie(cookie)
			if (creds.get('role') == '2') or (creds.get('role') == '1'):
				return render('/tools/masterCustList.mako')
			else:
				response.status_int = 404
				return

	'''
	   Returns the list of orders to be distributed
	   If user does not have access, throws 404
	'''
	def distribution(self):
		#look at cookie
		cookie = request.cookies.get("GFB_Cookie")
		if(cookie == None):
			response.status_int = 404
			return
		else:
			
			creds = Cookie.decryptCookie(cookie)
			if ((creds.get('role') == '3') or (creds.get('role') == '2') or (creds.get('role') == '1')) :
				return render('/tools/distOrders.mako')
			else:
				response.status_int = 404
				return
			
	'''
		Returns page for changing current user's password
	'''
	def changepassword(self):
		#look at cookie
		cookie = request.cookies.get("GFB_Cookie")
		if(cookie == None):
			response.status_int = 404
			return
		else:
			return render('/tools/changePassword.mako')
		
			
	'''
		Returns page that edits the current user's contact info
	'''
	def editprofile(self):
		#look at cookie
		cookie = request.cookies.get("GFB_Cookie")
		if(cookie == None):
			response.status_int = 404
			return
		else:
			return render('/tools/editProfile.mako')
		
	'''
		Returns page with confirmation info about order
	'''
	def confirm(self):
		return render('/tools/confirmOrder.php')
	
	'''
		Returns page with lists of pickup dates
	'''
	def pickupdates(self):
		return render('tools/pickupDates.mako')

	'''
		Returns page that user uses to signup
	'''
	def signup(self):
		return render('signup.mako')
	
	'''
		Returns page that admin uses to manage sample items
	'''
	def managesamples(self):
		return render('tools/sampleBoxes.mako')