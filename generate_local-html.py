#-------------------------------------------------------------------------------
# Name:        generate_local-html.py
# Purpose:
#
# Author:      Bob-Baig
#
# Created:     15/09/2013
# Copyright:   (c) Baig-Admin 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os

def generate_html():
    print("This program generates a web page to view all the files in a folder.")
    folder_path = input("Enter folder path: ")
    print(folder_path)
    os.chdir(folder_path)
    print(os.curdir)
    pic_list = os.listdir()
#   print(pic_list)
    dest_file = "index.html"
    file_handle = open(dest_file, 'w')
    for pic_name in pic_list:
        print("<img src = \"%s\">" % pic_name)
        file_handle.write("<img src = \"%s\">\n" % pic_name)
#   file_handle.close()     # Probably good practice to close the file
    os.chdir("C:\\")    # Make Python give-up control of the folder so it can be deleted
    input("Press any key to exit")

def main():
    generate_html()

if __name__ == '__main__':
    main()

