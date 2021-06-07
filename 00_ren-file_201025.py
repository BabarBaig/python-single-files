import os
import sys


def rename_files_in_cur_dir(cwd: str, str_old: str, str_new: str) -> str:
    print("\nIn dir:\t", cwd)
    resp: str = 'do_continue'
    for fn_old in os.listdir():
        if str_old not in fn_old:
            continue                # Current file is not a match.  Go to next one.
        fn_new: str = fn_old.replace(str_old, str_new)
        if resp == 'a':             # Doing a batch conversion
            print('Rename:\n' + fn_old + '\n' + fn_new)
        else:
            resp = input(fn_old + '\n' + fn_new + '\nRename? [Yes No All Reset newFolder Quit]\t')
        if resp == 'n':
            continue
        if resp == 'q':
            sys.exit(0)
        if resp == 'r':     # Reset search/replace
            break
        if resp == 'f':     # Change folder
            break
        if os.path.isfile(fn_new):
            print(fn_new, ' already exists! ********************')
            continue
        try:
            os.rename(fn_old, fn_new)
        except OSError as e:
            print('Error: Rename failed:', e)
    return resp


def rename_files(sub_dir: bool) -> None:
    """ Prompt use for a directory, an old string, and a new string.  In that directory,
    find files that containing the old string and replace it with the new string
    """
    cwd = os.getcwd()
    if sub_dir:
        cwd = cwd + '\\seen'
    prompt = 'Enter folder path [' + cwd + '] [Quit]:\n'
    if (resp := input(prompt)) == 'q':
        sys.exit(0)
    if resp != '':
        cwd = resp
    print('Switching to folder [' + cwd + ']')
    try:
        os.chdir(cwd)
    except OSError as e:
        print('Unable to open folder:', e)
    resp = 'x'
    while resp != 'f':      # Don't replace with: while 1.  See loop code.
        resp = str_old = input('\nEnter old string [Quit newFolder]:\t')
        if resp == 'f':
            continue
        if resp == 'q':
            sys.exit(0)
        resp = str_new = input('Enter new string [Quit newFolder]:\t')
        if resp == 'f':
            continue
        if resp == 'q':
            sys.exit(0)
        print('Replacing [' + str_old + '] with [' + str_new + ']')
        resp = rename_files_in_cur_dir(cwd, str_old, str_new)


if __name__ == '__main__':
    while 1:
        rename_files(False)
        rename_files(True)
