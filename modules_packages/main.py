from ecommerce.database import Database as DB

def main():
	print('Hello from main!')
	db = DB()
	db.print_db()

if __name__ == '__main__':
	main()
