# Use RELATIVE imports
from ..contact.email import send_mail

class Paypal():
	def print_paypal(self):
		# prod = ecommerce.products.Products()
		# prod.print_prod()
		print('Hello from Paypal!')
		send_mail()

def main():
	ppl = Paypal()
	ppl.print_paypal

if __name__ == '__main__':
	main()