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


if __name__ == '__main__':
    rename_file_dot_dash()
    x = input('Press any key to exit ...')
