import os
import sys


def rename_files_in_folder(folder_path: str, str_old: str, str_new: str) -> str:
    try:
        os.chdir(folder_path)
    except OSError as e:
        print('Unable to open folder:', e)
    print('\nSwitched to folder: ', folder_path, '\n')

    resp: str = None
    for fn_old in os.listdir():
        if str_old not in fn_old:       # If current file is not a match, goto next one.
            continue
        fn_new = fn_old.replace(str_old, str_new)
        if resp == 'a':                 # Doing a batch conversion.  Keep going
            print('Renaming ...\n' + fn_old + '\n' + fn_new + '\n')
        else:
            resp = input(fn_old + '\n' + fn_new + '\nRename? [All Yes No Reset Quit]\t')
        if resp == 'n':
            continue
        elif resp == 'r':  # Reset search/replace operation
            break
        elif resp == 'q':
            sys.exit(0)
        elif os.path.isfile(fn_new):
            print(fn_new, ' already exists! ********************\n')
            continue

        # If we've made it this far, we can rename
        try:
            os.rename(fn_old, fn_new)
            print('')
        except OSError as e:
            print('Error: Rename failed: ', e)
    return resp


# def Input(prompt: str) -> str:
#     if input 


def get_new_filename():
    """ Prompt user for a directory, an old string, and a new string.  In that directory,
    find files that containing the old string and replace it with the new string
    """

    if (fn_old := input('\nEnter old string [(Q)uit]:\t')) == 'q': sys.exit(0)
    print(fn_old)
    if (fn_new := input('Enter new string [(Q)uit]:\t'))   == 'q': sys.exit(0)
    print('Replacing [' + fn_old + '] with [' + fn_new + ']')
    return fn_old, fn_new


def rename_files():
    _FOLDER_PATH = os.getcwd()
    while True:
        fn_old, fn_new = get_new_filename()
        if rename_files_in_folder(_FOLDER_PATH, fn_old, fn_new) == 'r':
            continue
        rename_files_in_folder(_FOLDER_PATH + r'\000_Seen', fn_old, fn_new)


if __name__ == '__main__':
    rename_files()
