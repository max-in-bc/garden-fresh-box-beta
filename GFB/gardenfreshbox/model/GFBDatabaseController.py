import mysql.connector as ct
import datetime as date
import subprocess

#Database Controller Class
# Note this is the only controller which acts upon database, and also methods to turn them into the python models
class GFBDatabaseController():
    def __init__(self):
        
        #read db info from config file
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

    def addUser(self, email, password, firstName, lastName, credentials, hostSite, phoneNumber=None):
        q = "INSERT INTO Users (email, password, first_name, last_name, fk_credentials, phone_number, fk_hostsite_id) VALUES (%s, %s, %s, %s, %s, %s, %s);" 
        
        #call php script to compare user given password with hashed/salted stored password
        proc = subprocess.Popen("php -f gardenfreshbox/model/HashUserPassword.php " + password, shell=True, stdout=subprocess.PIPE)
        hashed_password = proc.stdout.read()
        info = (email,hashed_password,firstName,lastName,credentials,phoneNumber,hostSite)
        try:
            self.cursor.execute(q, info)
            self.cnx.commit()
            return True
        except ct.IntegrityError:
            return False
        return False

    def addUserModel(self, user):
        return self.addUser(user.email, user.password, user.firstName, user.lastName, user.credentialsIdFK, user.hostSite, user.phoneNumber)

    def authUser(self, email, password):
        q = "SELECT password FROM Users WHERE email='%s'" % email
        self.cursor.execute(q)
        result = self.cursor.fetchone()
        if result == None:
            return False
        
        #call php script to compare user given password with hashed/salted stored password
        proc = subprocess.Popen("php -f gardenfreshbox/model/AuthorizeUser.php '" + password + "' '" + result[0] + "'", shell=True, stdout=subprocess.PIPE)
        is_valid = proc.stdout.read()

        if is_valid == "1":
            return True
        return False
    
    def changePassword(self, email, oldPass, newPass):
        if self.authUser(email, oldPass):
            
            
             #call php script to compare user given password with hashed/salted stored password
            proc = subprocess.Popen("php -f gardenfreshbox/model/HashUserPassword.php " + newPass, shell=True, stdout=subprocess.PIPE)
            hashed_password = proc.stdout.read()
            q = "UPDATE Users SET password=%s WHERE email=%s" 
            info = (hashed_password, email)
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

    def updateUserModel(self, user, newEmail):
        return self.updateUser(user.email, newEmail, user.password, user.firstName, user.lastName, user.phoneNumber, user.hostSite, user.credentialsIdFK)

    def updateUser(self, email, newEmail, newPassword, newFirstName, newLastName, newPhoneNumber, hostSite, credentials):
        q = "UPDATE Users SET email=%s, first_name=%s, last_name=%s, phone_number=%s, fk_credentials=%s, fk_hostsite_id=%s WHERE email=%s" 
        info = (newEmail, newFirstName, newLastName, newPhoneNumber, credentials,hostSite, email)
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
    
    def removeUser(self,userID):
        q = "DELETE FROM Users WHERE id=%s"
        info = (userID,)
        self.cursor.execute(q, info)
        self.cnx.commit()
        affected_rows = self.cursor.rowcount
        if affected_rows:
            return True
        return False

    def getUsers(self, sortid):
        sortdict = {}
        sortdict['First Name'] = 'first_name'
        sortdict['Last Name'] = 'last_name'
        sortdict['Phone'] = 'phone_number'
        sortdict['Email'] = 'email'
        sortdict['Host Site'] = 'fk_hostsite_id'
        sortdict['Role'] = 'fk_credentials'
        
        q = "SELECT * FROM Users ORDER BY " + sortdict[sortid]
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

    #add hours to table then add new host site and associate new hours
    def addHostSite(self, name, address, city, province, postalCode, phoneNumber, email, coordinatorIDs, hoursofOperation):
        q = "INSERT INTO HoursOperation (sunday,monday,tuesday,wednesday,thursday,friday,saturday) VALUES (%s,%s,%s,%s,%s,%s,%s)" 
        info = (hoursofOperation['sunday'],hoursofOperation['monday'],hoursofOperation['tuesday'],hoursofOperation['wednesday'],hoursofOperation['thursday'],hoursofOperation['friday'],hoursofOperation['saturday'])
        try:
            self.cursor.execute(q, info)
            hours_id = self.cursor.lastrowid
        except Exception as e:
            return False
        q = "INSERT INTO HostSites (name,address,city,province,postal_code,phone_number,email,hours_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)" 
        info = (name,address,city,province,postalCode,phoneNumber,email,hours_id)
        try:
            self.cursor.execute(q, info)
            self.cnx.commit()
        except Exception as e:
            return False
        return True

    def addHostSiteModel(self, hostSite):
        self.addHostSite(hostSite.name, hostSite.address, hostSite.city, hostSite.province, hostSite.postalCode, hostSite.phone, hostSite.email, None, hostSite.hoursOfOperation)

    def updateHostSite(self, hostSiteID, name, address, city, province, postalCode, phoneNumber, email, coordinatorIDs, hoursofOperation):
        q = "INSERT INTO HoursOperation (sunday,monday,tuesday,wednesday,thursday,friday,saturday) VALUES (%s,%s,%s,%s,%s,%s,%s)" 
        info = (hoursofOperation['sunday'],hoursofOperation['monday'],hoursofOperation['tuesday'],hoursofOperation['wednesday'],hoursofOperation['thursday'],hoursofOperation['friday'],hoursofOperation['saturday'])
        self.cursor.execute(q, info)
        hours_id = self.cursor.lastrowid
        q = "UPDATE HostSites SET name=%s, address=%s, city=%s, province=%s, postal_code=%s, hours_id=%s, phone_number=%s, email=%s WHERE id=%s" 
        info = (name, address, city, province, postalCode, hours_id, phoneNumber, email, hostSiteID)
        self.cursor.execute(q, info)
        self.cnx.commit()

    def updateHostSiteModel(self, hostSite):
        self.updateHostSite(hostSite.id, hostSite.name, hostSite.address, hostSite.city, hostSite.province, hostSite.postalCode, hostSite.phone, hostSite.email, None, hostSite.hoursOfOperation)

    def removeHostSite(self,hostSiteID):
        q = "DELETE FROM HostSites WHERE id=%s"
        info = (hostSiteID,)
        self.cursor.execute(q, info)
        self.cnx.commit()
        affected_rows = self.cursor.rowcount
        if affected_rows:
            return True
        return False

    def getAssociatedHostSiteByEmail(self, email):
        q = "SELECT fk_hostsite_id FROM Users WHERE email ='%s'" % email
        self.cursor.execute(q)
        result = self.cursor.fetchone()
        if result is not None:
            site_id = result[0]
            
            q = "SELECT * FROM HostSites WHERE id ='%s'" % site_id
            self.cursor.execute(q)
            result = self.cursor.fetchone()
            return self.__createHostSiteDict(result)
        else: 
            return None
    
    def getHostSiteList(self, coordinatorID):
        return True

    def getAllHostSites(self, sortid):
        sortdict = {}
        sortdict['Name'] = 'name'
        sortdict['Address'] = 'address'
        sortdict['Hours'] = 'name'
        sortdict['Phone'] = 'phone_number'
        q = "SELECT * FROM HostSites ORDER BY " + sortdict[sortid]
        self.cursor.execute(q)
        results = self.cursor.fetchall()
        sites = []
        for site in results:
            hdict = self.__createHostSiteDict(site)
            sites.append(hdict)
        return sites

    def getHostSiteByName(self, name):
        q = 'SELECT * FROM HostSites WHERE name="%s"' % name
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
        q = "SELECT * FROM HoursOperation WHERE id='%s'" % hoursID
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

    def createNewOrder(self, dateCreated, dateToDistribute, firstName, lastName, email, phoneNumber, shouldSendNotifications, smallBoxQuantity,largeBoxQuantity, donations, donationReceipt, address, totalPaid, hostSitePickupID, hostSiteOrderID, vouchers, customerID):
        q = ("INSERT INTO Orders (distribution_date, creation_date, customer_first_name, "
                +    "customer_last_name, customer_email, customer_phone, email_notifications, "
                +    "large_quantity, small_quantity, donation, donation_receipt, total_paid, "
                +    "hostsitepickup_idFK, hostsitecreated_idFK, fk_user_id) "
                +    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

        info =        (dateToDistribute, dateCreated, firstName, lastName, email, phoneNumber,
                    shouldSendNotifications, largeBoxQuantity, smallBoxQuantity, donations,
                    donationReceipt, totalPaid, hostSitePickupID, hostSiteOrderID, customerID)
        try: 
            self.cursor.execute(q, info)
            self.cnx.commit()
            return True

        except Exception as e:
            return False

    def createEditOrderModel(self, order):
        return self.updateOrder(order.orderId, order.creationDate, order.distributionDate, order.customerFirstName, order.customerLastName, order.customerEmail, order.customerPhone, order.emailNotifications, order.smallQuantity, order.largeQuantity, order.donation, order.donationReceipt, order.totalPaid, order.hostsitepickupIdFK, order.hostsitecreatedIdFK, None, order.customerID)

    def updateOrder(self, orderID, dateCreated, dateToDistribute, firstName, lastName, email, phoneNumber, shouldSendNotifications, smallBoxQuantity,largeBoxQuantity, donations, donationReceipt, totalPaid, hostSitePickupID, hostSiteOrderID, vouchers, customerID):
        q = ("UPDATE Orders SET distribution_date=%s, creation_date=%s, customer_first_name=%s, "
                +    "customer_last_name=%s, customer_email=%s, customer_phone=%s, email_notifications=%s, "
                +    "large_quantity=%s, small_quantity=%s, donation=%s, donation_receipt=%s, total_paid=%s, "
                +    "hostsitepickup_idFK=%s, hostsitecreated_idFK=%s, fk_user_id=%s "
                +    "WHERE id=%s")

        info =        (dateToDistribute, dateCreated, firstName, lastName, email, phoneNumber,
                    shouldSendNotifications, largeBoxQuantity, smallBoxQuantity, donations,
                    donationReceipt, totalPaid, hostSitePickupID, hostSiteOrderID, customerID,orderID)
        try: 
        	self.cursor.execute(q, info)
          	self.cnx.commit()
        	return True

        except Exception as e:
    	    print e
            return False
        
    def deleteOrder(self, orderID):
        q = "DELETE FROM Orders WHERE id=%s"
        info = (orderID,)
        try: 
            self.cursor.execute(q, info)
            self.cnx.commit()
            return True

        except Exception as e:
            return False

    def createNewOrderModel(self, order):
        return self.createNewOrder(order.creationDate, order.distributionDate, order.customerFirstName, order.customerLastName, order.customerEmail, order.customerPhone, order.emailNotifications, order.smallQuantity, order.largeQuantity, order.donation, order.donationReceipt, None, order.totalPaid, order.hostsitepickupIdFK, order.hostsitecreatedIdFK, None, order.customerID)

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
        odict['fk_user_id'] = str(order[15])
#         
#         if odict['email_notifications'] == "off":
#             odict['email_notifications'] = "0"
#         elif odict['email_notifications'] == "on":
#             odict['email_notifications'] = "1"
#         
#         if odict['donation_receipt'] == "off":
#             odict['donation_receipt'] = "0"
#         elif odict['donation_receipt'] == "on":
#             odict['donation_receipt'] = "1"
       
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

    def getAllOrdersByHostSite(self, hid, sortid):
        sortdict = {}
        sortdict['Pickup Site'] = 'hostsitepickup_idFK'
        sortdict['Pickup Date'] = 'distribution_date'
        sortdict['Customer'] = 'customer_last_name'
        sortdict['Phone'] = 'customer_phone'
        sortdict['Email'] = 'customer_email'
        sortdict['No. Small'] = 'small_quantity'
        sortdict['No. Large'] = 'large_quantity'
        sortdict['Paid'] = 'total_paid'
        sortdict['Ordered On'] = 'creation_date'
        
        
        q = "SELECT * FROM Orders WHERE hostsitepickup_idFK=" + str(hid) + " ORDER BY " + sortdict[sortid]
        self.cursor.execute(q)
        orders = self.cursor.fetchall()
        return self.__separateListOrders(orders)
    
    def getAllOrdersByHostSiteName(self, hostsite):
        q = "SELECT * FROM Orders,HostSites WHERE name=%s"
        info = (hostsite,)
        self.cursor.execute(q, info)
        orders = self.cursor.fetchall()
        return self.__separateListOrders(orders)
    
    def sortOrdersModel(self, user_id, sort_id):
        sortdict = {}
        sortdict['Pickup Site'] = 'hostsitepickup_idFK'
        sortdict['Pickup Date'] = 'distribution_date'
        sortdict['Customer'] = 'customer_last_name'
        sortdict['Phone'] = 'customer_phone'
        sortdict['Email'] = 'customer_email'
        sortdict['No. Small'] = 'small_quantity'
        sortdict['No. Large'] = 'large_quantity'
        sortdict['Paid'] = 'total_paid'
        sortdict['Ordered On'] = 'creation_date'
        
        q = "SELECT * FROM Orders WHERE fk_user_id=%s AND (large_quantity > 0 OR small_quantity > 0) ORDER BY " +sortdict[sort_id]
        info = (user_id,)
        self.cursor.execute(q, info)
        orders = self.cursor.fetchall()
        return self.__separateListOrders(orders)    
    
    def getOrdersByUserID(self, user_id):
        q = "SELECT * FROM Orders WHERE fk_user_id=%s AND (large_quantity > 0 OR small_quantity > 0) ORDER BY distribution_date"
        info = (user_id,)
        self.cursor.execute(q, info)
        orders = self.cursor.fetchall()
        return self.__separateListOrders(orders)    
    
    def getOrdersByOrderID(self, order_id):
        q = "SELECT * FROM Orders WHERE id=%s AND (large_quantity > 0 OR small_quantity > 0)"
        info = (order_id,)
        self.cursor.execute(q, info)
        orders = self.cursor.fetchone()
        return self.__createOrderDict(orders)    
    
    def getDonationsByUserID(self, user_id):
        q = "SELECT * FROM Orders WHERE fk_user_id=%s AND large_quantity = 0 AND small_quantity = 0  ORDER BY creation_date"
        info = (user_id,)
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
        q = "SELECT * FROM Orders WHERE (hostsitepickup_idFK=%s) AND total_paid > 0 AND (distribution_date BETWEEN %s AND %s)"
        info = (hostSiteID, beginDate, endDate)
        self.cursor.execute(q, info)
        orders = self.cursor.fetchall()
        return self.__separateListOrders(orders)

    def getAllUnpaidOrdersByDistributionDate(self, beginDate, endDate):
        q = "SELECT * FROM Orders WHERE total_paid > 0 AND (distribution_date BETWEEN %s AND %s)"
        info = (beginDate, endDate)
        self.cursor.execute(q, info)
        orders = self.cursor.fetchall()
        return self.__separateListOrders(orders)

    def getPaidOrdersByDistributionDate(self, hostSiteID, beginDate, endDate):
        return True

    def getAllPaidOrdersByDistributionDate(self, beginDate, endDate):
        return True
    
         ###  DATE METHODS ###
    def addNewSampleItem(self, item, is_small_box):
        q = "INSERT INTO SampleBoxes (item, is_small_box) VALUES (%s, %s)"

        info = (item, is_small_box)
        try: 
            self.cursor.execute(q, info)
            self.cnx.commit()
            return True

        except Exception as e:
            return False
    
    def updateSampleItem(self, sample_id, item, is_small_box):
        q = "UPDATE SampleBoxes SET item=%s, is_small_box=%s WHERE id=%s"
        info = (item, is_small_box, sample_id)
        try:
            self.cursor.execute(q, info)
            self.cnx.commit()
        except Exception as e:
            return False
        return True
    
    def deleteSampleItem(self, sample_id):
        q = "DELETE FROM SampleBoxes WHERE id=%s"
        info = (sample_id,)
        self.cursor.execute(q, info)
        self.cnx.commit()
        affected_rows = self.cursor.rowcount
        if affected_rows:
            return True
        return False
    
    def getSampleItem(self, item_id):
        q = "SELECT * FROM SampleBoxes WHERE id='%s'" % item_id
        self.cursor.execute(q)
        result = self.cursor.fetchone()
        if result is not None:
            return self.__createSampleBoxDict(result)
        else: 
            return None
        
        ###  DATE METHODS ###
    def addNewDate(self, pickup_date, order_date):
        q = "INSERT INTO PickupDates (pickup_due, order_due) VALUES (%s, %s)"

        info = (pickup_date, order_date)
        try: 
            self.cursor.execute(q, info)
            self.cnx.commit()
            return True

        except Exception as e:
            return False
    
    def updateDate(self, date_id, pickup_date, order_date):
        q = "UPDATE PickupDates SET pickup_due=%s, order_due=%s WHERE id=%s"
        info = (pickup_date, order_date, date_id)
        try:
            self.cursor.execute(q, info)
            self.cnx.commit()
        except Exception as e:
            return False
        return True
    
    def deleteDate(self, date_id):
        q = "DELETE FROM PickupDates WHERE id=%s"
        info = (date_id,)
        self.cursor.execute(q, info)
        self.cnx.commit()
        affected_rows = self.cursor.rowcount
        if affected_rows:
            return True
        return False

    def getDate(self, date_id):
        q = "SELECT * FROM PickupDates WHERE id='%s'" % date_id
        self.cursor.execute(q)
        result = self.cursor.fetchone()
        if result is not None:
            return self.__createDateDict(result)
        else: 
            return None
        
    def __createDateDict(self, date):
        odict = {}
        odict['id'] = str(date[0])
        odict['pickup_date'] = str(date[1])
        odict['order_date'] = str(date[2])
        return odict
    
    def __separateDates(self, dates):
        date_records = []
        for record in dates:
            temp = self.__createDateDict(record)
            date_records.append(temp)
        return date_records
    
    def getAllPickupDates(self):
        q = "SELECT * FROM PickupDates ORDER BY order_due" 
        self.cursor.execute(q)
        dates = self.cursor.fetchall()
        return self.__separateDates(dates)    
    
    def __createSampleBoxDict(self, sample):
        odict = {}
        odict['id'] = str(sample[0])
        odict['item'] = str(sample[1])
        odict['is_small_box'] = str(sample[2])
        return odict
    
    def __separateSampleBoxes(self, samples):
        sample_records = []
        for record in samples:
            temp = self.__createSampleBoxDict(record)
            sample_records.append(temp)
        return sample_records
    
    def getSampleBoxItems(self):
        q = "SELECT * FROM SampleBoxes WHERE is_small_box = 1" 
        self.cursor.execute(q)
        r = self.cursor.fetchall()
        smallboxes = self.__separateSampleBoxes(r)  
        
        q2 = "SELECT * FROM SampleBoxes WHERE is_small_box = 0" 
        self.cursor.execute(q2)
        r2 = self.cursor.fetchall()
        largeboxes = self.__separateSampleBoxes(r2)  
        
        return smallboxes, largeboxes
