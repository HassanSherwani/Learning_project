from twilio.rest import TwilioRestClient
import time

# constants initialization

FROM = "+31" # twilio number with Dutch code
CALLED = "+31" # target
ACCOUNT_SID = ""
AUTH_TOKEN= ""


class Call:

	def __init__(self):
		self.FROM = FROM
		self.CALLED = CALLED
		self.ACCOUNT_SID = ACCUNT_SID
		self.AUTH_TOKEN = AUTH_TOKEN
		self.callCounter=0 # iterates with calls
		self.LIMITS=20 # limit of ongoing calls before an exit

	def set_target(self):
		self.CALLED= str(input("Enter ph no. of target, use '+1' before:"))

	def makeCall(self):
		client=TwilioRestClient(self.ACCOUNT_SID,self,AUTH_TOKEN)
		# CALL LOOP
		while self.callCounter < self.LIMIT:
			call=client.call.create(
			to= self.CALLED, from = self.FROM
			url="SAMPLE URL")
			self.callCounter=self.callCounter + 1
			print("Call No." + str(self.callCounter) + "Calling number:" + str(self.CALLED))
			time.sleep(10)
def main ():
	robo=Call()
	robo.set_target()
	robo.makecall()

if __name__ ==" __main__":
	main()