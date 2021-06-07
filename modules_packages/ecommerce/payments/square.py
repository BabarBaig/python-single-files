# Use RELATIVE imports
from ..database import Database
from ..products import Products

class Square():
	def print_square(self):
		db = Database()
		db.print_db()
		print('Hello from Square!')
