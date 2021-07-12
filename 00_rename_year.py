""" By design this is a one-pass solution to convert a
filename using date format yymmdd to yyyy-mm=dd """

import os


def getnewfn(fn: str) -> str:
    if not fn[:6].isdigit():
        return None
    fn_new = '20' + fn[0:2] + '-' + fn[2:4] + '-' + fn[4:]
    return fn_new


def date_reformat() -> None:
    tgt_folder = os.getcwd()
    resp = input(f'Enter home dir:\n{tgt_folder}\n')
    if len(resp) > 1:       # User provided a new folder path
        tgt_folder = resp
    print(f'Switching to folder [{tgt_folder}]')
    try:
        os.chdir(tgt_folder)
    except OSError as e:
        print('Unable to open folder:', e)
        return

    do_prompt: bool = True
    fn_new: str = None
    for fn in os.listdir():
        if (fn_new := getnewfn(fn)) is None:        continue
        if do_prompt:
            resp = input(f'Rename:\n    {fn}\n{fn_new}\n[yes, no, all, quit?\t')
        if resp == 'q':     break
        if resp == 'a':     do_prompt = False
        if resp == 'n':     continue
        try:
            os.rename(fn, fn_new)
        except:
            print('Rename failed!')

if __name__ == '__main__':
    date_reformat()
    print()
