# Use ABSOLUTE imports
import ecommerce.products
import ecommerce.database

class Stripe():
	def print_stripe(self):
		prod = ecommerce.products.Products()
		prod.print_prod()
		print('Hello from Stripe!')
