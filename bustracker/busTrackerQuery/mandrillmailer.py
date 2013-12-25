# Import smtplib for the actual sending function
import smtplib
import mandrill
import datetime

class MandrilMessagelMailer:
	
	def __init__(self, string):
		self.mandrill_client = mandrill.Mandrill('FS0x0tqzlI6bv5asv9UIuQ')
		self.status = self.send(string)
		print self.status
		
	def send(self,string):
		try:
			message = {
				'from_email': 'jorge.silva.jetter@gmail.com',
				'from_name': 'Jorge Silva',
				'headers': {'Reply-To': 'jorge.silva.jetter@gmail.com'},
				'html': '<p>' + string + '</p>',
				'subject': string,
				'text': string,
				'to': [{'email': 'jorge.silva.jetter@gmail.com','name': 'Jorge Silva','type': 'to'}]
			}
			result = self.mandrill_client.messages.send(
				message=message, 
				async=False, 
			)
			return result[0]['status']
		except mandrill.Error, e:
			# Mandrill errors are thrown as exceptions
			print 'A mandrill error occurred: %s - %s' % (e.__class__, e)
			# A mandrill error occurred: <class 'mandrill.UnknownSubaccountError'> - No subaccount exists with the id 'customer-123'    
			raise