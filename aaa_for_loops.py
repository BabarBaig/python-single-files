'''
Demo for() loops with increasing complexity
'''

def for_01():
	squares = [1, 4, 9, 16, 25, 36, 49, 64, 81]
	sum = 0
	for num in squares:
		sum += num
	print(sum)	# 285

def for_02():
	sum = 0
	for i in range (10):
		sum += i * i
	print(sum)	# 285

def for_03():
	"""
	Demo for() loop with start value 2, end value 10, and a jump of 2
	Demo formatted print() with 2 numbers that change with every loop
	"""
	for x in range(2, 11, 2):
		print("Square of %d is %d" % (x, x*x))

if __name__ == '__main__':
	for_01()
	for_02()
	for_03()
# end
