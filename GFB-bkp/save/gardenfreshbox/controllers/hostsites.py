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
	   Returns html formatted tables for get requests
	'''
	def host_site(self):
		db = DB()
		# Get request - if hostSiteId is *, all host sites are returned, else only the host site matching given hostSiteID
		if (request.method == "GET"):
			hostSiteID = request.params['hostSiteID']
			if hostSiteID == '*':
				hs = db.getAllHostSites()
				return HostSite.toTable(hs)
			else:
				hs = db.getHostSite(hostSiteID)
				return json.dumps(hs)

		# Put request - if hostSiteID is empty string, a new host site is added, else the host with with hostSiteID is updated
		elif (request.method == "PUT"):
			print request.params
			hostSiteID = request.params['hostSiteID']
			if(hostSiteID == ""):
				print request.params
				# New host site
				hs = HostSite(request.params['name'], request.params['address'], request.params['city'], request.params['province'], request.params['postalCode'], request.params['hoursOfOperation'], request.params['phone'])
				success = db.addHostSiteModel(hs)
				if success:
					return HostsitesController.trueStr
				else:
					return "{\"success\":\"fasle\", \"message\":\"Unable to add new host site\"}"
			else:
				# update host site
				hs = HostSite(request.params['name'], request.params['address'], request.params['city'], request.params['province'], request.params['postalCode'], request.params['hoursOfOperation'], request.params['phone'])
				hs.id = hostSiteID
				success = db.updateHostSiteModel(hs)
				if success:
					return HostsitesController.trueStr
				else:
					return "{\"success\":\"fasle\", \"message\":\"Unable to add new host site\"}"

		# Delete request - not supported
		elif (request.method == "DELETE"):
			return "{\"success\":\"false\", \"message\":\"Delete request is unimplemented\"}"

	'''
	   This method returns a raw JSON dump of information for all host sites
	'''
	def hsJSON(self):
		db = DB()
		if (request.method == "GET"):
			return json.dumps(db.getAllHostSites())
