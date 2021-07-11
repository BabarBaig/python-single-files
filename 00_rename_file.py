import os
import sys


def rename_files_in_cur_dir(str_old: str, str_new: str) -> None:
    dont_prompt: bool = False

    for fn_old in os.listdir():
        if str_old not in fn_old:
            continue                # Current file is not a match.  Go to next one.
        fn_new: str = fn_old.replace(str_old, str_new)

        if dont_prompt:
            print(f'Rename:\n{fn_old}\n{fn_new}')
        else:
            resp = input(f'{fn_old}\n{fn_new}\nRename? [Yes No All Reset Quit]?\t')
            if resp == 'a':
                dont_prompt = True
            if resp == 'n':
                continue
            if resp == 'r':     # Reset search/replace
                break

        if os.path.isfile(fn_new):
            print(fn_new, ' already exists! ********************')
            continue

        try:
            os.rename(fn_old, fn_new)
        except OSError as e:
            print('Error: Rename failed:', e)
            sys.exit(0)


def get_old_new_fn() -> None:
    """ Rename files by replacing str_old with str_new.
    """
    do_continue: bool = True
    str_old = 'str_old'
    str_new = 'str_new'
    str_old = input('\nEnter old string [Quit newFolder]:\t')
    if str_old == 'q':
        sys.exit(0)
    if str_old == 'f':
        do_continue = False
    else:
        str_new = input('Enter new string [Quit Reset]:\t')
        if str_new == 'q':
            sys.exit(0)
        if str_new == 'r':
            do_continue = False
    if do_continue:
        print(f'Replacing [{str_old}] with [{str_new}]')
    return do_continue, str_old, str_new


def switch_folder(folder: str) -> None:
    print(f'Switching to folder [{folder}]')
    try:
        os.chdir(folder)
    except OSError as e:
        print('Unable to open folder:', e)
        sys.exit(0)


def rename_files_main() -> None:
    """ Based on how this Python script is executed, cwd can be C:\\Windows\\System32, or
    C:\\Users\\BabBa, or the correct folder.  Get to folder where target files are located.
    """
    cwd = os.getcwd()
    resp = input(f'Enter home dir:\n{cwd}\n')
    if len(resp) > 1:
        cwd = resp

    # do_continue: bool = True
    while 1:
        switch_folder(cwd)

        str_old = input('\nEnter old string [Quit]:\t')
        if str_old == 'q':
            sys.exit(0)

        str_new = input('Enter new string [Quit]:\t')
        if str_new == 'q':
            sys.exit(0)

        rename_files_in_cur_dir(str_old, str_new)

        if (do_continue := switch_folder(cwd+'\\000_Seen')) == False:
            break
        if (do_continue := rename_files_in_cur_dir(str_old, str_new)) == False:
            break


def y2_y4_digit() -> None:
    """Change [yymmdd] to [yyyy-mm-dd]"""
    print('In y2_y4_digit()')


if __name__ == '__main__':
    if (resp := input(  "\na: Change [yymmdd] to [yyyy-mm-dd]"
                        "\nb: Rename files (default)"
                        "\nEnter option (q to quit):\t : ")) == 'q':
        print()
        sys.exit(0)
    if resp == 'a':
        y2_y4_digit()
    else:
        rename_files_main()
    print("\n")
