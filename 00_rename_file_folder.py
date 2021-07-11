#import calendar        # for monthrange()
#import codecs
#import tkinter
import os

# =~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~

def index_html_jpg():
	f = open("index.html", "w")
	#f.write('<html>\n')
	#f.write('<head></head>\n')
	#f.write('<body>\n')
	for fn in os.listdir():
		if srch_str not in fn:
			continue
		write_str = '<img src ="' + fn + '">\n'
		f.write(write_str)
	#f.write('<body>\n')
	#f.write('</html>\n')
	f.close()

def read_unicode():
	f = codecs.open('foo.txt', 'rU', 'utf-8')
	for line in f:
		pass  # here line is a *unicode* string

# =~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~

def rename_dir_O1():
	''' in dir_base, locate dirs with substring srch_str, and repl with
	repl_str instead '''
	dir_base = input('Enter base folder: ')
	os.chdir(dir_base)
	print('cd to ' +os.getcwd())
	srch_str = input('Enter search string: ')
	repl_str = input('Enter replacement string: ')
	print('Replace [' + srch_str + '] with [' + repl_str + ']')
	for cur_name in os.listdir():
		if os.path.isdir(cur_name) and srch_str in cur_name:
			# Now, replace srch_str with repl_str to generate new dir name
			new_name = cur_name.replace(srch_str, repl_str)
			resp = input('Rename [' + cur_name + '] to [' + new_name + '] [y, n, x]? ')
			if resp == 'x':
				return
			elif resp == 'y':
				os.rename(cur_name, new_name)

def rename_dir_02():
	''' in dir_base, locate dirs with substring srch_str, and repl with
	repl_str instead '''
	dir_base = input('Enter base folder:\n')
	print('cd to:\n' + os.getcwd())
	os.chdir(dir_base)
	srch_str = input('Enter search string:\n')
	repl_str = input('Enter replacement string:\n')
	print('Replace [' + srch_str + '] with [' + repl_str + ']')
	for cur_item in os.listdir():
		if not os.path.isdir(cur_item):
			continue            # skip files
		if not srch_str in cur_item:
			print('Skipping: ', cur_item)
			continue            # current folder may already have right format
		# By now cur_item is a folder that should be renamed
		new_name = cur_item.replace(srch_str, repl_str)
		#Use following line only if there are multiple duplicates
		#new_name = new_name + '1'
		print('Rename [', cur_item, '] to [', new_name,']')
		os.rename(cur_item, new_name)

def delete_mt_dir():
	dir_base = input('Enter base folder:\n')
	os.chdir(dir_base)
	print('cd to:\n' + os.getcwd())

	# remove empty subfolders
	for file in os.listdir():
		if not os.path.isdir(file):
			continue
		# By now we know [file] is a folder.  Is it empty?
		subfolderfiles = os.listdir(file)
		if len(subfolderfiles) > 0:
			continue
		user_input = input('Delete [' + file + '] [y, n, x]? ')
		if user_input == 'y':
			os.rmdir(file)
		elif user_input == 'x':
			return

# =~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~

def move_file(folder_source, folder_dest, oldfn_before, year, oldfn_after,
			  fn_before, fn_after):
	for month in range(1, 13):
		month_str_zpad = str(month).zfill(2)
		days_in_month = calendar.monthrange(year, month)[1]
		old_fn = oldfn_before + str(year) + month_str_zpad + str(days_in_month) + oldfn_after
		print(old_fn)
		new_fn = fn_before + month_str_zpad + fn_after
		print(new_fn)
		#os.rename(old_fn, new_fn)
		from shutil import move
		move(folder_source+'/'+old_fn, folder_dest + '/'+ new_fn)

def rename_fn_06(start_folder, fn):
	os.chdir(start_folder)
	filepath = get_fn(start_folder)
	oldfn = os.path.split(filepath)[1]
	root_phrase_1 = 'VDI2014-'
	root_phrase_2 = ' Fidelity.pdf'
	counter = '01'
	new_fn = root_phrase_1 + counter + root_phrase_2
	os.rename(oldfn, new_fn)

def rename_fn_04(start_folder, oldfn_before, oldfn_after, fn_before, fn_after):
	os.chdir(start_folder)
	for i in range(1, 3):
		i_str_zpad = str(i).zfill(2)
		old_fn = oldfn_before + i_str_zpad + oldfn_after
		new_fn = fn_before + i_str_zpad + fn_after
		os.rename(old_fn, new_fn)

def rename_fn_01(start_folder, oldfn_before, year, start_mth, end_mth, oldfn_after, fn_before, fn_after):
	""" Great for renaming Fidelity statements, which use the last day of the month in their name: State02282014.pdf """
	dir_base = tkinter.filedialog.askdirectory(initialdir=r'C:\Users\Owner\Downloads')
	os.chdir(dir_base)
	for month in range(start_mth, end_mth + 1):
		month_str_zpad = str(month).zfill(2)
		days_in_month = calendar.monthrange(year, month)[1]
		old_fn = oldfn_before + month_str_zpad + str(days_in_month) + str(year) + oldfn_after
		new_fn = fn_before + str(year) + '-' + month_str_zpad + fn_after
		do_exit = input('Rename [' + old_fn + '] to [' + new_fn + '].  Press "x" to exit')
		if do_exit == 'x':  break
		try:    os.rename(old_fn, new_fn)
		except: print('Failed rename [' + old_fn + '] to [' + new_fn + ']')

def rename_file_prompt(start_folder, str_old, str_new):
	for oldfn in os.listdir():
		if str_old in oldfn:
			newfn = oldfn.replace(str_old, str_new)
			resp = input('[' + oldfn + '] > \n[' + newfn + ']? [y, n, x] ')
			if resp == 'y':
				os.rename(oldfn, newfn)
			elif   resp == 'x':
				break

def rename_files():
	''' Prompt use for a directory, an old string, and a new string.  In that directory,
	find files that containg the old string and replace it with the new string
	'''
	#import tkinter.messagebox
	#tkinter.messagebox.showinfo('Enter an old string and new string to rename files')
	#import tkinter.filedialog
	#dir_base = tkinter.filedialog.askdirectory()
	os.chdir(dir_base)
	str_old = tkinter.simpledialog.askstring('', 'Enter old string to replace: ')
	str_new = tkinter.simpledialog.askstring('', 'Enter new string: ')

	for fn_old in os.listdir():
		if str_old not in fn_old:
			continue
		fn_new = fn_old.replace(str_old, str_new)
		resp = tkinter.messagebox.askyesnocancel(title='Confirm file rename',
										   message = 'Rename\n' + fn_old + ' >> to\n' + fn_new + '?')
		if   (resp is None):  return
		elif (resp == False): continue
		os.rename(fn_old, fn_new)

# =~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~

if __name__ == '__main__':
	#create_index_html()
	#delete_mt_dir()
	rename_dir_02()
	#rename_files()
