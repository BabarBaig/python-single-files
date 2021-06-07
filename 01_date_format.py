import os

def reformat2(fn: str) -> bool:
	return False

def getnewfn(fn: str) -> str:
	if not fn[:6].isdigit():
		return None
	fn_new = '20' + fn[0:2] + '-' + fn[2:4] + '-' + fn[4:]
	return fn_new

def date_reformat() -> None:
	print('In folder:', os.getcwd())
	doprompt: bool = True
	for fn in os.listdir():
		fn_new: str = getnewfn(fn)
		if fn_new is None:
			continue
		if doprompt:
			resp = input('Rename:\n' + '    ' + fn + '\n' + fn_new + ' [yes, no, all, quit? ')
		if resp == 'q':
			exit()
		if resp == 'a':
			doprompt = False
		if resp == 'n':
			continue
		try:
			os.rename(fn, fn_new)
		except:
			print('Rename failed!')

if __name__ == '__main__':
	date_reformat()
	print('Press any key to exit ...')
	_ = input()
