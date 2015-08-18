import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from ast import literal_eval
from gardenfreshbox.lib.base import BaseController, render

from gardenfreshbox.model.cookie import Cookie
from gardenfreshbox.model.hostsite import HostSite
from gardenfreshbox.model.GFBDatabaseController import GFBDatabaseController as DB

import json

log = logging.getLogger(__name__)

class HostsitesController(BaseController):
	trueStr = "{\"success\":\"true\"}"

	'''
	   This method recieves get and put requests for host sites 
	   Calls database methods when necessary
	   Returns html formatted tables or json for get requests
	'''
	def host_site(self):
		db = DB()

		# Get request - if hostSiteId is *, all host sites are returned, else only the host site matching given hostSiteID
		if (request.method == "GET"):
			hostSiteID = request.params['hostSiteID']
			if hostSiteID == '*':
				hs = db.getAllHostSites(request.params['sortid'])
				return HostSite.toTable(hs, request.params['staticTable'] == "true")
			else:
				hs = db.getHostSite(hostSiteID)
				return json.dumps(hs)

		# Put request - if hostSiteID is empty string, a new host site is added, else the host with with hostSiteID is updated
		elif (request.method == "PUT"):
			hostSiteID = request.params['hostSiteID']
			
			if (request.params['hostSiteID'] != "" and request.params['name'] == ""):
				# Delete existing host site	
				success = db.removeHostSite(hostSiteID)
				if success:
					return self.trueStr
				else:
					return "{\"success\":\"false\", \"message\":\"Unable to delete new host site\"}"
							
			elif(hostSiteID == ""):
				# New host site
				hs = HostSite(request.params['name'], request.params['address'], request.params['city'], request.params['province'], request.params['postalCode'], request.params['hoursOfOperation'], request.params['phone'], request.params['email'])
				success = db.addHostSiteModel(hs)
				if success:
					return self.trueStr
				else:
					return "{\"success\":\"false\", \"message\":\"Unable to add new host site\"}"
			else:
				# Update existing host site
				hs = HostSite(request.params['name'], request.params['address'], request.params['city'], request.params['province'], request.params['postalCode'], request.params['hoursOfOperation'], request.params['phone'], request.params['email'])
				hs.id = hostSiteID
				success = db.updateHostSiteModel(hs)
				if success:
					return self.trueStr
				else:
					return "{\"success\":\"false\", \"message\":\"Unable to update host site\"}"

		# Delete request - not supported
		elif (request.method == "DELETE"):
			return "{\"success\":\"false\", \"message\":\"Unimplemented\"}"

	'''
	   This method returns a raw JSON dump of information for all host sites
	   Note: No confidential info
	'''
	def hsJSON(self):
		db = DB()
		if (request.method == "GET"):
			return json.dumps(db.getAllHostSites("Name"))
