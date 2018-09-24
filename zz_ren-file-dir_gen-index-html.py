#import calendar         # for monthrange()
#import codecs
import os
# =========================================================
#import tk           # Only works for Python 3
#import Tkinter          # Only works for Python 2
import tkinter as tk
import tkinter.filedialog
import tkinter.simpledialog
# =========================================================

def file_read():
    ''' f.readlines() reads the whole file into memory and returns a list of lines.
    f.read() reads the whole file into a single string, which can be a useful with regular
    expressions. '''
    pass

def file_wite(my_list):
    f = open("zz_Delete.Me.txt", "w")   # 'a' append, 'r' read, 'rU' smart \n
    for item in my_list:
        f.write(str(item) + "\n")
    f.close()

def file_wite_test():
    # Generate a list of squares of the numbers 1-10 using list comprehension.
    my_list = [i**2 for i in range(1,11)]
    file_wite(my_list)

def read_unicode():
    f = codecs.open('foo.txt', 'rU', 'utf-8')
    for line in f:
        pass  # here line is a *unicode* string

# =~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~

def move_file(folder_source, folder_dest, oldfn_before, year, oldfn_after, fn_before, fn_after):
    for month in range(1, 13):
        month_str_zpad = str(month).zfill(2)
        days_in_month = calendar.monthrange(year, month)[1]
        old_fn = oldfn_before + str(year) + month_str_zpad + str(days_in_month) + oldfn_after
        print(old_fn)
        new_fn = fn_before + month_str_zpad + fn_after
        print(new_fn)
#       os.rename(old_fn, new_fn)
        from shutil import move
        move(folder_source+'/'+old_fn, folder_dest + '/'+ new_fn)

def rename_dir_IO():
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

def rm_mt_dir(path):
    if not os.path.isdir(path):
        print('[' + path + '] is not a directory')
        return

    # remove empty subfolders
    files = os.listdir(path)
    if len(files):  # Reduce indentation here
        for f in files:
            fullpath = os.path.join(path, f)
            if os.path.isdir(fullpath):
                rm_mt_dir(fullpath)

    # if folder is empty, delete it
    files = os.listdir(path)
    if len(files) ==  0:
        user_input = input('Delete [' + path + '] [y, n, x] ')
        if user_input == 'y':
            os.rmdir(path)
        elif user_input == 'x':
            return

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

    os.chdir(start_folder)
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
    os.chdir(start_folder)
    for oldfn in os.listdir():
        if str_old in oldfn:
            newfn = oldfn.replace(str_old, str_new)
            resp = input('[' + oldfn + '] > \n[' + newfn + ']? [y, n, x] ')
            if resp == 'y':
                os.rename(oldfn, newfn)
            elif   resp == 'x':
                break

# =~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~

def ch_dir():
    dir_base = tk.filedialog.askdirectory(initialdir=r'C:\Users\Owner\Downloads')
    os.chdir(dir_base)

def zero_pad_fn():
    ch_dir()
    fn_prefix = tk.simpledialog.askstring('', 'Enter fn_prefix to zero-pad: ')
    fn_suffix = tk.simpledialog.askstring('', 'Enter fn_suffix to zero-pad: ')
    for i in range(1, 10):
        fn_old = fn_prefix       + str(i) + fn_suffix
        fn_new = fn_prefix + '0' + str(i) + fn_suffix
        resp = tk.messagebox.askyesnocancel(title='Confirm file rename',
                message = 'Rename\n' + fn_old + ' >> to\n' + fn_new + '?')
        if   (resp is None):  return -1
        elif (resp == False): continue
        os.rename(fn_old, fn_new)

def rename_dirs(dir_base):
    ''' in dir_base, locate dirs with substring srch_str, and rename them
    to repl_str instead
    '''
    ch_dir()
    srch_str = tk.simpledialog.askstring('', 'Enter old dir string to replace: ')
    repl_str = tk.simpledialog.askstring('', 'Enter new dir string: ')

    for srch_dir in os.listdir():
        if not(os.path.isdir(srch_dir) and srch_str in srch_dir):
            continue
        repl_dir = srch_dir.replace(srch_str, repl_str)
        resp = tk.messagebox.askyesnocancel(title='Confirm file rename',
                                	message = 'Rename\n' + srch_dir + ' >> to\n' + repl_dir + '?')
        if   (resp is None):  return -1
        elif (resp == False): continue
        os.rename(srch_dir, repl_dir)
    return 0

def rename_files():
    ''' Prompt use for a directory, an old string, and a new string.  In that directory,
    find files that containg the old string and replace it with the new string
    '''
    #default_dir = r'C:\Users\Owner\Downloads'
    dest_dir = tk.filedialog.askdirectory()
    #os.chdir(dest_dir)
    # ch_dir()
    str_old = tk.simpledialog.askstring('', 'Enter old string to replace: ')
    str_new = tk.simpledialog.askstring('', 'Enter new string: ')

    for fn_old in os.listdir():
        if str_old not in fn_old:
            print('[' + fn_old + '] skipped')
            continue
        fn_new = fn_old.replace(str_old, str_new)
        resp = tk.messagebox.askyesnocancel(title='Confirm file rename',
                message = 'Rename\n' + fn_old + ' >> to\n' + fn_new + '?')
        if   (resp is None):  return
        elif (resp == False): continue
        os.rename(fn_old, fn_new)

def create_index_html():
    default_dir = r'C:\Users\Owner\Downloads'
    dest_dir = tk.filedialog.askdirectory(initialdir=default_dir)
    os.chdir(dest_dir)
    # ch_dir()
    srch_str = tk.simpledialog.askstring('', 'Enter search string for index-html: ')
    f = open("index.html", "w")
    for fn in os.listdir():
        if srch_str not in fn:
            continue
        write_str = '<img src ="' + fn + '">\n'
        f.write(write_str)
    f.close()
    os.chdir(default_dir)

def main():
    # base_dir = r"C:\Users\Owner\Downloads"
    # clean_filename()
    # rename_fn_01('C:/Users/Babar/SkyDrive/Sync/02.VDI-Systems/VDI_Tax/VDI2014/VDI_Bills,Stmt,payroll',
    #               'document', 'VDI2014 Fidelity-', '.pdf')
    # rename_fn_05('C:/Users/Babar/Downloads',
    #              'C:/Users/Babar/SkyDrive/Sync/02.VDI-Systems/VDI_Tax/VDI2014/VDI_Bills,Stmt,payroll',
    #                'stmt_', 2014, '.pdf', 'VDI2014 DCU-', '.pdf')
    # rename_dir(r'F:\000\001.Dwnld', 'abcd', '')   # Note using raw text
    # rm_mt_dir(base_dir)
    # rename_dir_IO()
    # file_wite_test()
    # rename_fn_01(base_dir, 'Statement', 2014, 1, 10, '.pdf', 'JB2014 Fidelity ', '.pdf')
    # rename_fn_02(base_dir, 'PublicAgent ', 'PublicAgent.com ')
    # zero_pad_fn()
    rename_files()
    # create_index_html()

if __name__ == '__main__':
    main()
