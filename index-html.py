#-------------------------------------------------------------------------------
# Name:      generate_local-html.py
# Purpose:   This program generates a web page to view all the pics in a folder
#
# Author:    Bob Baig
#
# Created:   2013-09-20
# Copyright: (c) Bob Baig 2013
# Licence:   <your licence>
#-------------------------------------------------------------------------------

import os

def generate_index_html():
    folder_path = input("This program generates a web page to view all the "
        "files in a folder.  Enter folder path:\t")
    print(folder_path)
    os.chdir(folder_path)
    print(os.curdir)
    my_list = os.listdir()
    print(my_list)
    dest_file = "index.html"
    file_handle = open(dest_file, 'w')
    for pic_name in my_list:
        file_handle.write("<img src = \"%s\">\n" % pic_name)
    file_handle.close()
    os.chdir("C:\\")        # Move-away from the folder so it can be deleted

def main():
    generate_html()

if __name__ == '__main__':
    main()

