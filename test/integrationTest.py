from unittest import TestCase
import onechat
from onechat.client import Client
from onechat.message import FacebookTextMessage

class TestSendingMessage(TestCase):
	def setUp(self):
		self.client = Client("config.txt")
		#self.recepient = "10156942645370710"
		self.recepient = self.client.config.get('onechat','RECEPIENT')
		
	def test_facebook_text_message(self):
		message = FacebookTextMessage("test")
		print self.client.send(self.recepient, message)
