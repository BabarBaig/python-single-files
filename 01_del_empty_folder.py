import os


def dir_empty_delete():
    dir_base = input('Enter base folder:\n')
    os.chdir(dir_base)
    print('cd to:\n' + os.getcwd())

    # remove empty sub folders
    for file in os.listdir():
        if not os.path.isdir(file):
            continue
        # By now we know [file] is a folder.  Is it empty?
        sub_folder_files = os.listdir(file)
        if len(sub_folder_files) > 0:
            continue
        user_input = input('Delete [' + file + '] [y, n, x]? ')
        if user_input == 'y':
            os.rmdir(file)
        elif user_input == 'x':
            return


if __name__ == '__main__':
    dir_empty_delete()
