import os
import sys


def rename_file(fn_old: str, idx1: int, idx2: int, resp: str) -> str:
    fn_new = fn_old[0:idx1] + '-' + fn_old[idx1+1: idx2] + '-' + fn_old[idx2+1:]
    if resp == 'a':
        print(f'Rename:\n{fn_old}\n{fn_new}')
    else:
        resp = input(fn_old + '\n' + fn_new + '\nRename? [Yes All No Quit]\t')

    if resp == 'q':
        sys.exit(0)
    elif resp == 'n':
        return resp
    if os.path.isfile(fn_new):
        print(fn_new, ' already exists! ********************')
        return 'n'
    try:
        os.rename(fn_old, fn_new)
    except OSError as e:
        print('Error: Rename failed:', e)
        return 'e'
    return resp


def rename_file_dot_dash():
    resp: str = 'y'
    for fn_old in os.listdir():
        if len(fn_old) > 8 and fn_old[2] == '.' and fn_old[5] == '.':
            resp = rename_file(fn_old, 2, 5, resp)
        elif len(fn_old) > 10 and fn_old[4] == '.' and fn_old[7] == '.':
            resp = rename_file(fn_old, 4, 7, resp)


def rename_file_dt_sh_long2(fn_old: str, resp: str) -> str:
    """ Rename any fn of type 210506_abcd to 2021-05-06_abcd """
    fn_new = '20' + fn_old[0:2] + '-' + fn_old[2:4] + '-' + fn_old[4:]
    if resp == 'a':
        print(f'Rename:\n{fn_old}\n{fn_new}')
    else:
        resp = input('    ' + fn_old + '\n' + fn_new + '\nRename? [Yes All No Quit]\t')

    if resp == 'q':
        sys.exit(0)
    elif resp == 'n':
        return resp
    if os.path.isfile(fn_new):
        print(fn_new, ' already exists! ********************')
        return 'n'
    try:
        os.rename(fn_old, fn_new)
    except OSError as e:
        print('Error: Rename failed:', e)
        return 'e'
    return resp


def rename_file_dt_sh_long1():
    """ If 1st 6 chars of a fn are digits, we assume it's a short date and try to rename it to a long date """
    resp: str = 'y'
    for fn_old in os.listdir():
        if len(fn_old) >= 6:
            isadigit = True
            for i in range(6):
                if not fn_old[i].isdigit():
                    isadigit = False
                    break
            if isadigit:
                resp = rename_file_dt_sh_long2(fn_old, resp)


if __name__ == '__main__':
    rename_file_dt_sh_long1()
    rename_file_dot_dash()
    x = input('Press any key to exit ...')
