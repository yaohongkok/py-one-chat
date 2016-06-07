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
		print self.client.send(self.recepient, message)

	def testFacebookImageMessage(self):
		message = FacebookImageMessage("http://orig14.deviantart.net/9480/f/2015/307/5/1/annoying_dog_by_rabbit_cipher-d9ffdsu.gif")
		print self.client.send(self.recepient, message)
