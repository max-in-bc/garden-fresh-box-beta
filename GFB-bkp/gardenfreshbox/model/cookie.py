from operator import itemgetter
from Crypto.Cipher import AES
import json
import base64

class Cookie():
	
	def __init__(self):
		self.user_name = None
		self.email = None
		self.role = None
		self.host_site = None

	def __init__(self,user_name,email,role, host_site):
		self.user_name = user_name
		self.email = email
		self.role = str(role)
		self.host_site = str(host_site)

	def encryptCookie(self):
		dict = {"user_name" : str(self.user_name), "email" : str(self.email), "role" : str(self.role), "host_site" : str(self.host_site)}
		return self.encrypt(json.dumps(dict))

	def encrypt(self, message):
		if(len(message)%16 != 0):
			r = 16 - (len(message)) % 16
			for i in range(0,r):
				message = message + ' '

		cipher = AES.new('449jgrj4ojagfkngkk f9y5c',AES.MODE_ECB)
		encoded = base64.b64encode(cipher.encrypt(message))
		return encoded

	@staticmethod
	def decryptCookie(cookie):
		return json.loads(Cookie.decrypt(cookie))

	@staticmethod
	def decrypt(text):
		cipher = AES.new('449jgrj4ojagfkngkk f9y5c',AES.MODE_ECB)
		decode = cipher.decrypt(base64.b64decode(text))
		return decode
