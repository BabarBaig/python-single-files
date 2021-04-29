#-------------------------------------------------------------------------------
# Name:        create-index-html.py
# Purpose:
#
# Author:      Bob-Baig
#
# Created:     15/09/2013
# Copyright:   (c) Baig-Admin 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os

def generate_index_html():
    zero_pad = input('Do filenames have zero padding [y/n]? ')
    base_url = input('Enter base url: ')
    f = open("index.html", "w")   # 'a' append, 'r' read, 'rU' smart \n
    for i in range(1, 10):
        if (zero_pad == 'y'):
            f.write('<img src="' + base_url + '0' + str(i) + '.jpg">\n')
        else:
            f.write('<img src="' + base_url       + str(i) + '.jpg">\n')
    for i in range(10, 21):
        f.write('<img src="' + base_url + str(i) + '.jpg">\n')
    f.close()
    print('index.html generated')

def main():
    generate_index_html()

if __name__ == '__main__':
    main()
