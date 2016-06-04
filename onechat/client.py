from ConfigParser import SafeConfigParser
import requests

class Client(object):
	def __init__(self, configFileName):
		self.config = SafeConfigParser()
		self.config.read(configFileName)
	
	def send(self, recepient, message):
		if message.platform == "facebook":
			self.sendFacebookMessage(recepient, message)
		else:
			raise Exception('Unknown Message\' Platform')
	
	def sendFacebookMessage(self,recepient, message):
		token = self.config.get('onechat','FACEBOOK_MESSENGER_TOKEN')
		sendUrl = "https://graph.facebook.com/v2.6/me/messages?access_token=" + token
		
		try:
			response = requests.post(sendUrl, json=message.toPayload(recepient))
			print response.__dict__
			return response
		except Exception:
			print "Failed"
			return "Failed sending request"
