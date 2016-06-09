from abc import ABCMeta, abstractmethod

class Message(object):
	__metaclass__ = ABCMeta
	
	def __init__(self, text):
		self.text = text
		self.platform = None

	@abstractmethod
	def toPayload(self):
		pass

######################################################
# Facebook Messages
######################################################
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

class FacebookImageMessage(FacebookMessage):
	def __init__(self, imageUrl):
		super(FacebookImageMessage, self).__init__("")
		self.imageUrl = imageUrl
	
	def toPayload(self,recepient):
		jsonData = {
			"recipient": self.jsonIdOrPhone(recepient),
			"message": {
				"attachment": {
					"type": "image",
					"payload": {
						"url": self.imageUrl
					}
				}
			}
		}
		
		return jsonData

class FacebookButtonsInfo(object):
	def __init__(self, types=[], titles=[], urlsOrPayloads=[]):
		if((len(types)==len(titles)) and (len(types)==len(titles))):
			self.typeList = types
			self.titleList = titles
			self.urlOrPayloadList = urlsOrPayloads
		else:
			raise Exception('Unequal numbers of elements in input arguments')
		
	def toPayload(self):
		jsonData = []
		
		for i in range(0,len(self.typeList)):
			buttonDict = {
				"type": self.typeList[i],
				"title": self.titleList[i]
			}
			
			if(buttonDict["type"]=="web_url"):
				buttonDict["url"] = self.urlOrPayloadList[i]
			elif(buttonDict["type"]=="postback"):
				buttonDict["payload"] = self.urlOrPayloadList[i]
			else:
				raise Exception("Cannot find type of '"+ buttonDict["type"] +"'. Can only be 'web_url' or 'postback'.")
			
			jsonData.append(buttonDict)
		
		return jsonData

class FacebookGenericElement(object):
	def __init__(self, title=None, \
				item_url=None, image_url=None, subtitle=None, \
				buttons=None):
		if(title==None):
			raise Exception("'title' must not be none")
		else:
			self.title = title
			self.itemUrl = item_url
			self.imageUrl = image_url
			self.subtitle = subtitle
			self.facebookButtonsInfo = buttons
	
	def toPayload(self):
		jsonData = {"title": self.title}
		
		if(self.itemUrl != None):
			jsonData["item_url"] = self.itemUrl
		
		if(self.imageUrl != None):
			jsonData["image_url"] = self.imageUrl
		
		if(self.subtitle != None):
			jsonData["subtitle"] = self.subtitle
		
		if(self.facebookButtonsInfo != None):
			jsonData["buttons"] = self.facebookButtonsInfo.toPayload()
		
		return jsonData


class FacebookGenericMessage(FacebookMessage):
	def __init__(self, facebookGenericElements=[]):
		super(FacebookGenericMessage, self).__init__("")
		self.facebookGenericElementList = facebookGenericElements
	
	def toPayload(self,recepient):
		jsonData = {
			"recipient": self.jsonIdOrPhone(recepient),
			"message": {
				"attachment": {
					"type": "template",
					"payload": {
						"template_type":"generic",
						"elements":[]
					}
				}
			}
		}
		
		numberOfElements = len(self.facebookGenericElementList)
		
		for i in range(0,numberOfElements):
			jsonData["message"]["attachment"]["payload"]["elements"] \
				.append(self.facebookGenericElementList[i].toPayload()) 
		
		return jsonData

class FacebookButtonMessage(FacebookMessage):
	def __init__(self, text, buttons=None):
		super(FacebookButtonMessage, self).__init__(text)
		self.facebookButtonsInfo = buttons
	
	def toPayload(self,recepient):
		jsonData = {
			"recipient": self.jsonIdOrPhone(recepient),
			"message": {
				"attachment": {
					"type": "template",
					"payload": {
						"template_type":"button",
						"text": self.text,
						"buttons":[]
					}
				}
			}
		}
		
		if (self.facebookButtonsInfo!=None):
			 jsonData["message"]["attachment"]["payload"]["buttons"] = self.facebookButtonsInfo.toPayload()
		
		return jsonData
