import os
import sys


def switch_folder(folder: str) -> None:
    print(f'Switching to folder [{folder}]')
    try:
        os.chdir(folder)
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
            resp = input(f'{fn_old}\n{fn_new}\nRename? [Yes(default) No All Reset Quit]?\t')
            if resp == 'q':     sys.exit(0)
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
    cwd = os.getcwd()
    resp = input(f'Enter home dir:\n{cwd}\n')
    if len(resp) > 1:       # User provided a new folder path
        cwd = resp

    while True:
        switch_folder(cwd)
        if (str_old := input('\nEnter old string [Quit]:\t')) == 'q':       sys.exit(0)
        if (str_new := input(  'Enter new string [Quit]:\t')) == 'q':       sys.exit(0)
        rename_files_in_cur_dir(str_old, str_new)
        switch_folder(cwd+'\\000_Seen')
        rename_files_in_cur_dir(str_old, str_new)


if __name__ == '__main__':
    rename_files()

