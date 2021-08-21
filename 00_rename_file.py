import os
import sys


def my_input(prompt: str):
    if (resp := input(prompt)) == 'q':
        sys.exit(0)
    return resp


def switch_folder() -> None:
    cwd = os.getcwd()
    resp = input(f'Enter home dir:\n{cwd}\n')
    if len(resp) > 1:       # User provided a new folder path
        cwd = resp
    print(f'\nSwitching to folder [{cwd}]')

    try:
        os.chdir(cwd)
    except OSError as e:
        print('Unable to open folder:', e)
        sys.exit(0)


def rename_files_in_cur_dir(str_old: str, str_new: str) -> None:
    do_prompt: bool = True
    for fn_old in os.listdir():
        if str_old not in fn_old:
            continue                # Current file is not a match.  Go to next one.
        fn_new: str = fn_old.replace(str_old, str_new)
        if do_prompt:
            resp = my_input(f'{fn_old}\n{fn_new}\nRename? [Yes(default) No All Reset Quit]?\t')
            if resp == 'n':     continue
            if resp == 'a':     do_prompt = False
            if resp == 'r':     break       # Reset search/replace
        else:
            print(f'Rename:\n{fn_old}\n{fn_new}')

        if os.path.isfile(fn_new):
            print(fn_new, ' already exists! ********************')
            continue

        try:
            os.rename(fn_old, fn_new)
        except OSError as e:
            print('Error: Rename failed:', e)
            sys.exit(0)


def rename_files() -> None:
    """ Based on how this Python script is executed, cwd can be C:\\Windows\\System32, or
    C:\\Users\\BabBa, or the correct folder.  Get to folder where target files are located.
    NOTE: We rename files in current folder and its subfolder before asking for new str_old str_new.
    """

    while True:
        str_old = my_input('\nEnter old string [Quit]:\t')
        str_new = my_input(  'Enter new string [Quit]:\t')
        rename_files_in_cur_dir(str_old, str_new)


if __name__ == '__main__':
    switch_folder()
    rename_files()

