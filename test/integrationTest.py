from unittest import TestCase
import onechat
from onechat.client import Client
from onechat.message import *

class TestSendingMessage(TestCase):
	def setUp(self):
		self.client = Client("config.txt")
		self.recepient = self.client.config.get('onechat','RECEPIENT')
		
	def testFacebookTextMessage(self):
		message = FacebookTextMessage("test")
		response = self.client.send(self.recepient, message)
		self.assertEqual(response.status_code,200)

	def testFacebookImageMessage(self):
		message = FacebookImageMessage("http://orig14.deviantart.net/9480/f/2015/307/5/1/annoying_dog_by_rabbit_cipher-d9ffdsu.gif")
		response = self.client.send(self.recepient, message)
		self.assertEqual(response.status_code,200)
		
	def testFacebookGenericMessage(self):
		facebookButtonsInfo = FacebookButtonsInfo(\
			types=["web_url","postback","web_url"], \
			titles=["Button A", "Button B", "Button C"],\
			urlsOrPayloads=["http://www.build2master.com", "B", "http://www.build2master.com"])
		
		facebookGenericElement1 = FacebookGenericElement(\
			title="Element Title 1", item_url="http://www.build2master.com",\
			image_url="http://www.build2master.com/uploads/3/7/3/4/37345271/7877270.png",\
			subtitle="Build-2-Master has awesome articles", buttons=facebookButtonsInfo)
		
		facebookGenericElement2 = FacebookGenericElement(title="Element Title 2",subtitle="Great!")
		
		facebookGenericElements = [facebookGenericElement1, facebookGenericElement2]
		
		message = FacebookGenericMessage(facebookGenericElements)
		response = self.client.send(self.recepient, message)
		self.assertEqual(response.status_code,200)

	def testFacebookButtonMessage(self):
		facebookButtonsInfo = FacebookButtonsInfo(\
			types=["web_url","postback","web_url"], \
			titles=["Button A", "Button B", "Button C"],\
			urlsOrPayloads=["http://www.build2master.com", "B", "http://www.build2master.com"])
		
		message = FacebookButtonMessage("A, B or C?", facebookButtonsInfo)
		response = self.client.send(self.recepient, message)
		self.assertEqual(response.status_code,200)
