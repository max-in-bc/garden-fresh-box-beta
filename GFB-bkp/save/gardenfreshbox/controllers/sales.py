import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from ast import literal_eval
from gardenfreshbox.lib.base import BaseController, render
from gardenfreshbox.model.cookie import Cookie
from gardenfreshbox.model.sale import Sale
from gardenfreshbox.model.GFBDatabaseController import GFBDatabaseController as DB
import json

log = logging.getLogger(__name__)

class SalesController(BaseController):

	# used for returning success messages
	trueString = "{\"success\":\"true\"}"

	'''
	   This funciton accepts get and put requests
	'''
	def sales(self):
		db = DB()	

		# for all sales (regardless of host site) send hostSiteName : *
		if (request.method == "GET"):
			if request.params['hostSiteName'] == "*":
				orderList = db.getAllOrders()
				return Sale.toTableMasterOrderList(orderList)
			else:	
				orderList = db.getAllOrders()
				return Sale.toCashSaleList(orderList, request.params['hostSiteName']);
		
		# uses orderID as a key, if it is sent as "" a new order is added
		# updating orders was not implemented 
		elif (request.method == "PUT"):				
			if request.params['orderID'] == "":
				order = Sale(None, request.params['dateCreated'], request.params['dateToDistribute'], request.params['firstName'], request.params['lastName'], request.params['email'], request.params['phoneNumber'], request.params['shouldSendNotifications'], request.params['smallBoxQuantity'],request.params['largeBoxQuantity'], request.params['donations'], request.params['donationReceipt'], request.params['totalPaid'], request.params['hostSitePickupID'],request.params['hostSiteOrderID'])
				success = db.createNewOrderModel(order)
				if success:
					return self.trueString
				else:
					return "{\"success\":\"false\",\"message\":\"Failed to enter new order.\"}"
			else:
				# order = Sale(request.params['orderID'], request.params['dateCreated'], request.params['dateToDistribute'], request.params['firstName'], request.params['lastName'], request.params['email'], request.params['phoneNumber'], request.params['shouldSendNotifications'], request.params['smallBoxQuantity'],request.params['largeBoxQuantity'], request.params['donations'], request.params['donationReceipt'], request.params['totalPaid'], request.params['hostSitePickupID'],request.params['hostSiteOrderID'])
				return "{\"success\":\"false\",\"message\":\"Failed to enter new order.\"}"

	'''
	   This method gets all orders to be sent to a given host site
	'''
	def dist(self):
		db = DB()	
		if (request.method == "GET"):
			orderList = db.getAllOrders()
			return Sale.toDistList(orderList, request.params['hostSiteName']);

	'''
	   This method gets a list of all customers and returns it as a pretty html table
	   A 404 is thrown if the request does not have enough access
	'''
	def customers(self):
		cookie = request.cookies.get("FCS_GFB_Cookie")
		if(cookie == None):
			response.status_int = 404
			return
		else:
			creds = Cookie.decryptCookie(cookie)	
			if(creds.get('role') == '2') or (creds.get('role') == '1'):
				db = DB()
				customerList = db.getAllCustomers()
				return Sale.toTableMasterCustomerList(customerList);
			else:
				response.status_int = 404
				return

	'''
	   This method gets a list of all donors and returns in a pretty html table
	   A 404 is thrown if the request does not have enough access
	'''
	def donors(self):
		cookie = request.cookies.get("FCS_GFB_Cookie")
		if(cookie == None):
			response.status_int = 404
			return
		else:
			creds = Cookie.decryptCookie(cookie)
			if (creds.get('role') == '1' or creds.get('role') == '2'):
				db = DB()
				donorList = db.getDonationOrders()			
				return Sale.toTableDonations(donorList);
			else:
				response.status_int = 404
				return
