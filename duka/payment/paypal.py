import sys
from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient(object):
	"""docstring for PayPalCleint"""
	def __init__(self):
		self.client_id ='AfCvT5ReE513VNIDHr70E-7NIb2my2N7-rwB-PrEB0fJozQa4-DC-nU7hJeS9w4j_LHoR_L2TLiT4Px-'
		self.client_secret ='ECq-kkhC6nfDk4Jq5uFgG46XmR7xqrjvULEF_jS371wgyC4BU8LRhwjxc0fgZuwOKTulN1v5nUc9f7TU'
		self.enviroment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
		self.client = PayPalHttpClient(self.enviroment)


