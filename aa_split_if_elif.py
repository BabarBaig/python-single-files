
# Parse command line > break it into tokens using split() > read first token
# as a Python command > execute it.

def func1():
	with open("aa_split_if_elif.txt","r") as f:
		content = f.readlines()
	list1 = []
	for line in content:
		cmd1 = line.split()[0];
		if (cmd1 == 'insert'):
			cmd1, val1, index1 = line.split()
			list1.insert(int(val1), int(index1))
		elif (cmd1 == 'print'):
			print(list1)
		elif (cmd1 == 'remove'):
			cmd1, index1 = line.split()
			list1.remove(int(index1))
		elif (cmd1 == 'append'):
			cmd1, val1 = line.split()
			list1.append(int(val1))
		elif (cmd1 == 'sort'):
			list1.sort()
		elif (cmd1 == 'pop'):
			list1.pop()
		elif (cmd1 == 'reverse'):
			list1.reverse()

if __name__ == '__main__':
	func1()
