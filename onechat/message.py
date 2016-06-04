from abc import ABCMeta, abstractmethod

class Message(object):
	__metaclass__ = ABCMeta
	
	def __init__(self, text):
		self.text = text
		self.platform = None

	@abstractmethod
	def toPayload(self):
		pass

class FacebookMessage(Message):
	def __init__(self, text):
		super(FacebookMessage, self).__init__(text)
		self.platform = "facebook"
	
	def jsonIdOrPhone(self,recepient):
		if(recepient.find("+")==True):
			return {"phone_number": recepient}
		else:
			return {"id": recepient}

class FacebookTextMessage(FacebookMessage):
	def __init__(self, text):
		super(FacebookTextMessage, self).__init__(text)
	
	def toPayload(self,recepient):
		jsonData = {
			"recipient": self.jsonIdOrPhone(recepient),
			"message": {"text":self.text}
		}
		
		return jsonData
