import mysql.connector as ct
import datetime as date

class GFBDatabaseController():
	def __init__(self):
		f = open('gardenfreshbox/model/db_config.csv', 'r')       
		f.readline()
		params = f.readline()
		params_split = params.split(',')
		params_split[-1] = params_split[-1][:-1]

		self.cnx = ct.connect(host=params_split[0], user=params_split[1], password=params_split[2], database=params_split[3])
		self.cursor = self.cnx.cursor()

	#####################
	###  USER METHODS ###
	#####################

	def userExists(self, email):
		if email is False:
			return False
		email = '"' + email + '"'
		q = "SELECT * FROM Users WHERE email=%s;" % email
		self.cursor.execute(q)
		results = self.cursor.fetchall()
		if not results:
			return False
		else:
			return True

	def addUser(self, email, password, firstName, lastName, credentials, phoneNumber=None):
		q = "INSERT INTO Users (email, user_password, first_name, last_name, fk_credentials_id, phone) VALUES (%s, %s, %s, %s, %s, %s);" 
		info = (email,password,firstName,lastName,credentials,phoneNumber)
		try:
			self.cursor.execute(q, info)
			self.cnx.commit()
			return True
		except ct.IntegrityError:
			return False
		return False

	def addUserModel(self, user):
		return self.addUser(user.email, user.password, user.firstName, user.lastName, user.credentialsIdFK, user.phoneNumber)

	def authUser(self, email, password):
		q = "SELECT user_password FROM Users WHERE email='%s'" % email
		self.cursor.execute(q)
		result = self.cursor.fetchone()
		if result == None:
			return False
		if result[0] == password:
			return True
		return False

	def updateUserModel(self, user):
		return self.updateUser(user.email, user.newEmail, user.password, user.firstName, user.lastName, user.phoneNumber, None, user.credentialsIdFK)

	def updateUser(self, email, newEmail, newPassword, newFirstName, newLastName, newPhoneNumber, hostSites, credentials):
		q = "UPDATE Users SET email=%s, user_password=%s, first_name=%s, last_name=%s, phone=%s, fk_credentials_id=%s WHERE email=%s" 
		info = (newEmail, newPassword, newFirstName, newLastName, newPhoneNumber, credentials, email)
		try:
			self.cursor.execute(q, info)
			result = self.cursor.rowcount
			self.cursor.fetchone()
			self.cnx.commit()
			if result > 0:
				return True
		except ct.IntegrityError:
			return False

		return False

	def getUsers(self):
		q = "SELECT * FROM Users"
		self.cursor.execute(q)
		results = self.cursor.fetchall()
		users = []
		for entry in results:
			udict = self.__createUserDict(entry)
			users.append(udict)
		return users

	def getUser(self, email):
		q = "SELECT * FROM Users WHERE email='%s'" % email
		self.cursor.execute(q)
		result = self.cursor.fetchone()
		udict = self.__createUserDict(result)
		return udict

	def __createUserDict(self, result):
		udict = {}
		udict['id'] = result[0]
		udict['email'] = result[1]
		udict['password'] = result[2]
		udict['first_name'] = result[3]
		udict['last_name'] = result[4]
		udict['phone_number'] = str(result[5])
		udict['fk_credentials'] = result[6]
		udict['fk_hostsite_id'] = result[7]
		return udict


	##########################
	###  HOST SITE METHODS ###
	##########################

	def getCoordinatorList(self, hostSiteID):
		return True

	def hostSiteNameExists(self, name):
		result = self.getHostSiteByName(name)
		if not result:
			return False
		return True

	def addHostSite(self, name, address, city, province, postalCode, phoneNumber, coordinatorIDs, hoursofOperation):
		q = "INSERT INTO HostHours (sunday,monday,tuesday,wednesday,thursday,friday,saturday) VALUES (%s,%s,%s,%s,%s,%s,%s)" 
		info = (hoursofOperation['sunday'],hoursofOperation['monday'],hoursofOperation['tuesday'],hoursofOperation['wednesday'],hoursofOperation['thursday'],hoursofOperation['friday'],hoursofOperation['saturday'])
		try:
			self.cursor.execute(q, info)
			hours_id = self.cursor.lastrowid
		except Exception as e:
			return False
		q = "INSERT INTO HostSites (id, site_name,address,city,province,postal_code,phone,fk_hours_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)" 
		info = (hours_id, name,address,city,province,postalCode,phoneNumber,hours_id)
		try:
			self.cursor.execute(q, info)
			self.cnx.commit()
		except Exception as e:
			return False
		return True

	def addHostSiteModel(self, hostSite):
		self.addHostSite(hostSite.name, hostSite.address, hostSite.city, hostSite.province, hostSite.postalCode, hostSite.phone, None, hostSite.hoursOfOperation)

	def updateHostSite(self, hostSiteID, name, address, city, province, postalCode, phoneNumber, coordinatorIDs, hoursofOperation):
		q = "INSERT INTO HostHours (sunday,monday,tuesday,wednesday,thursday,friday,saturday) VALUES (%s,%s,%s,%s,%s,%s,%s)" 
		info = (hoursofOperation['sunday'],hoursofOperation['monday'],hoursofOperation['tuesday'],hoursofOperation['wednesday'],hoursofOperation['thursday'],hoursofOperation['friday'],hoursofOperation['saturday'])
		self.cursor.execute(q, info)
		hours_id = self.cursor.lastrowid
		q = "UPDATE HostSites SET site_name=%s, address=%s, city=%s, province=%s, postal_code=%s, fk_hours_id=%s, phone=%s WHERE id=%s" 
		info = (name, address, city, province, postalCode, hours_id, phoneNumber, hostSiteID)
		self.cursor.execute(q, info)
		self.cnx.commit()

	def updateHostSiteModel(self, hostSite):
		self.updateHostSite(hostSite.id, hostSite.name, hostSite.address, hostSite.city, hostSite.province, hostSite.postalCode, hostSite.phone, None, hostSite.hoursOfOperation)

	def removeHostSite(self,hostSiteID):
		q = "DELETE FROM HostSites WHERE id=%s"
		info = (hostSiteID,)
		self.cursor.execute(q, info)
		self.cnx.commit()
		affected_rows = self.cursor.rowcount
		if affected_rows:
			return True
		return False

	# TODO - relationship between host sites and coordinators
	def getHostSiteList(self, coordinatorID):
		return True

	def getAllHostSites(self):
		q = "SELECT * FROM HostSites"
		self.cursor.execute(q)
		results = self.cursor.fetchall()
		sites = []
		for site in results:
			hdict = self.__createHostSiteDict(site)
			sites.append(hdict)
		return sites

	def getHostSiteByName(self, name):
		q = "SELECT * FROM HostSites WHERE name ='%s'" % name
		self.cursor.execute(q)
		result = self.cursor.fetchone()
		if result is not None:
			return self.__createHostSiteDict(result)
		else: 
			return None

	def getHostSite(self, hostSiteID):
		q = "SELECT * FROM HostSites WHERE id='%s'" % hostSiteID
		self.cursor.execute(q)
		result = self.cursor.fetchone()
		if result is not None:
			return self.__createHostSiteDict(result)
		else:
			return None

	def __getHostHours(self, hoursID):
		q = "SELECT * FROM HostHours WHERE id='%s'" % hoursID
		self.cursor.execute(q)
		result = self.cursor.fetchone()
		hours_dict = self.__createHoursOpDict(result)
		return hours_dict

	def __createHoursOpDict(self, hours):
		hdict = {}
		if hours is None:
			hdict['sunday'] = ""
			hdict['monday'] = ""
			hdict['tuesday'] = ""
			hdict['wednesday'] = ""
			hdict['thursday'] = ""
			hdict['friday'] = ""
			hdict['saturday'] = ""
		hdict['sunday'] = hours[1]
		hdict['monday'] = hours[2]
		hdict['tuesday'] = hours[3]
		hdict['wednesday'] = hours[4]
		hdict['thursday'] = hours[5]
		hdict['friday'] = hours[6]
		hdict['saturday'] = hours[7]
		return hdict

	def __createHostSiteDict(self, host_site):
		hdict = {}
		hdict['id'] = host_site[0]
		hdict['name'] = host_site[1]
		hdict['address'] = host_site[2]
		hdict['city'] = host_site[3]
		hdict['province'] = host_site[4]
		hdict['postal_code'] = host_site[5]
		hdict['phone_number'] = host_site[6]
		hdict['email'] = host_site[7]
		hdict['hours_of_operation'] = self.__getHostHours(host_site[8])
		return hdict

	######################
	###  ORDER METHODS ###
	######################

	def createNewOrder(self, dateCreated, dateToDistribute, firstName, lastName, email, phoneNumber, shouldSendNotifications, smallBoxQuantity,largeBoxQuantity, donations, donationReceipt, address, totalPaid, hostSitePickupID, hostSiteOrderID, vouchers):
		q = ("INSERT INTO Orders (distribution_date, creation_date, customer_first_name, "
				+	"customer_last_name, customer_email, customer_phone, email_notifications, "
				+	"large_quantity, small_quantity, donation, donation_receipt, total_paid, "
				+	"hostsitepickup_idFK, hostsitecreated_idFK) "
				+	"VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

		info =		(dateCreated, dateToDistribute, firstName, lastName, email, phoneNumber,
					shouldSendNotifications, largeBoxQuantity, smallBoxQuantity, donations,
					donationReceipt, totalPaid, hostSitePickupID, hostSiteOrderID)
		try: 
			self.cursor.execute(q, info)
			self.cnx.commit()
			return True

		except Exception as e:
			print e
			return False

	def createNewOrderModel(self, order):
		return self.createNewOrder(order.creationDate, order.distributionDate, order.customerFirstName, order.customerLastName, order.customerEmail, order.customerPhone, order.emailNotifications, order.smallQuantity, order.largeQuantity, order.donation, order.donationReceipt, None, order.totalPaid, order.hostsitepickupIdFK, order.hostsitecreatedIdFK, None)

	def getDonationOrders(self):
		q = "SELECT * FROM Orders WHERE donation>0"
		self.cursor.execute(q)
		results = self.cursor.fetchall()
		return self.__separateListOrders(results)

	def getAllOrders(self):
		q = "SELECT * FROM Orders"
		self.cursor.execute(q)
		results = self.cursor.fetchall()
		return self.__separateListOrders(results)

	def __separateListOrders(self, orders):
		donations = []
		for order in orders:
			temp = self.__createOrderDict(order)
			donations.append(temp)
		return donations

	def __createOrderDict(self, order):
		odict = {}
		odict['id'] = str(order[0])
		odict['distribution_date'] = str(order[1])
		odict['creation_date'] = str(order[2])
		odict['customer_first_name'] = str(order[3])
		odict['customer_last_name'] = str(order[4])
		odict['customer_email'] = str(order[5])
		odict['customer_phone'] = str(order[6])
		odict['email_notifications'] = str(order[7])
		odict['large_quantity'] = str(order[8])
		odict['small_quantity'] = str(order[9])
		odict['donation'] = str(order[10])
		odict['donation_receipt'] = str(order[11])
		odict['total_paid'] = str(order[12])
		odict['hostsitecreated_idFK'] = str(order[13])
		odict['hostsitepickup_idFK'] = str(order[14])
		return odict

	def getAllCustomers(self):
		q = "SELECT * FROM Orders"
		self.cursor.execute(q)
		orders = self.cursor.fetchall()
		return self.__separateCustomers(orders)

	def __removeDuplicates(self, customers):
		result = [dict(tupleized) for tupleized in set(tuple(item.items()) for item in customers)]
		return result

	def __separateCustomers(self, orders):
		customers = []
		for order in orders:
			temp = self.__createCustomerDict(order)
			customers.append(temp)
		return self.__removeDuplicates(customers)

	def __createCustomerDict(self, order):
		odict = {}
		odict['customer_first_name'] = str(order[3])
		odict['customer_last_name'] = str(order[4])
		odict['customer_email'] = str(order[5])
		odict['customer_phone'] = str(order[6])
		odict['email_notifications'] = str(order[7])
		return odict

	def getCustomersByHostSite(self, hid):
		q = "SELECT * FROM Orders WHERE hostsitepickup_idFK='%s'" % hid
		self.cursor.execute(q)
		orders = self.cursor.fetchall()
		return self.__separateCustomers(orders)

	def updateOrder(self, orderID, dateCreated, dateToDistribute, firstName, lastName, email, phoneNumber, shouldSendNotifications, smallBoxQuantity,largeBoxQuantity, donations, totalPaid, hostSitePickupID, hostSiteOrderID, vouchers):
		q = "UPDATE Orders SET creation_date=%s, distribution_date=%s, customer_first_name=%s, customer_last_name=%s, customer_email=%s, customer_phone=%s, email_notifications=%s, small_quantity=%s, large_quantity=%s, donation=%s, total_paid=%s, hostsitepickup_idFK=%s, hostsitecreated_idFK=%s WHERE id=%s"
		info = (dateCreated, dateToDistribute, firstName, lastName, email, phoneNumber, shouldSendNotifications, smallBoxQuantity,largeBoxQuantity, donations, totalPaid, hostSitePickupID, hostSiteOrderID, orderID)
		try:
			self.cursor.execute(q, info)
			self.cnx.commit()
		except Exception as e:
			return False
		return True

	def removeOrder(self, orderID):
		return True

	def cancelOrder(self, orderID):
		return True

	def getAllOrdersByDistributionDate(self, beginDate, endDate):
		q = "SELECT * FROM Orders WHERE DATE(distribution_date) BETWEEN '%s' AND '%s'" % (str(beginDate), str(endDate))
		self.cursor.execute(q)
		orders = self.cursor.fetchall()
		return self.__separateListOrders(orders)	

	def getAllCanceledOrdersByDistributionDate(self, beginDate, endDate):
		return True


	def getAllOrdersByHostSite(self, hid):
		q = "SELECT * FROM Orders WHERE hostsitecreated_idFK=%s"
		info = (hid,)
		self.cursor.execute(q, info)
		orders = self.cursor.fetchall()
		return self.__separateListOrders(orders)

	def getOrderByDistributionDate(self, hostSiteID, beginDate, endDate):
		q = "SELECT * FROM Orders WHERE (hostsitepickup_idFK=%s) AND distribution_date BETWEEN %s AND %s" 
		info = (hostSiteID, beginDate, endDate)
		self.cursor.execute(q, info)
		orders = self.cursor.fetchall()
		return self.__separateListOrders(orders)

	def getUnpaidOrdersByDistributionDate(self, hostSiteID, beginDate, endDate):
		q = "SELECT * FROM Orders WHERE (hostsitepickup_idFK=%s) AND ((large_quantity*20) + (small_quantity*15) - total_paid) > 0 AND (distribution_date BETWEEN %s AND %s)"
		info = (hostSiteID, beginDate, endDate)
		self.cursor.execute(q, info)
		orders = self.cursor.fetchall()
		return self.__separateListOrders(orders)

	def getAllUnpaidOrdersByDistributionDate(self, beginDate, endDate):
		q = "SELECT * FROM Orders WHERE ((large_quantity*20) + (small_quantity*15) - total_paid) > 0 AND (distribution_date BETWEEN %s AND %s)"
		info = (beginDate, endDate)
		self.cursor.execute(q, info)
		orders = self.cursor.fetchall()
		return self.__separateListOrders(orders)

	def getPaidOrdersByDistributionDate(self, hostSiteID, beginDate, endDate):
		return True

	def getAllPaidOrdersByDistributionDate(self, beginDate, endDate):
		return True

#controller = GFBDatabaseController()
#controller.addUser('paulart@gmail.com', '1234', 'adfasdf', 'adsfasdfas', '1', 'adsfasdf')
#print controller.authUser('paul.blart@gmail.com', '2234')
#print controller.getUser('paul.blart@gmail.com')
#controller.getUsers()
#print controller.updateUser('pauly@gmail.com', 'paulyx2234@gmail.com' , '1234567', 'asdf', 'asdf', '1', 'adsf', '1')
#print controller.removeHostSite('52')
#tester = controller.getHostSite(1)
#controller.addHostSite('name', 'address', 'city', 'province', 'postalCode', 'phoneNumber', 'coordinatorIDs', tester['hours_of_operation'])
#controller.updateHostSite(1, "UpdatedName", "I dont know", "asdfasdf","I just dont care anymore", "nowhere", "adsf", [], tester['hours_of_operation'])
#controller.createNewOrder(None, None, "Paul", "Blart", "Paul@blart.com", "1234567890", 1, 10, 15, 20, 1, {}, 0, 1, 1, "")
#print len(controller.getAllCustomers())
#print len(controller.getCustomersByHostSite(1))
#print controller.getCustomersByHostSite(0)
#print len(controller.getAllOrdersByDistributionDate(date.datetime(2014, 4, 7), date.datetime(2014, 4, 8)))
#print len(controller.getOrderByDistributionDate(1, date.datetime(2014,01,01), date.datetime(2014,12,12)))
#print (controller.getOrderByDistributionDate(1, date.datetime(2014,01,01), date.datetime(2014,12,12)))
#print (controller.updateOrder(1, date.datetime(2012,01,01), date.datetime(2012,01,01), "Paul", "blart", "asdf", "adgag", 1,1,1,1,1,1,1,1))
#print len(controller.getUnpaidOrdersByDistributionDate(1, date.datetime(2012,01,01), date.datetime(2014,12,12)))
