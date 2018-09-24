<<<<<<< HEAD
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     Write a Scrabble cheater
#
# Author:      Baig-Admin
#
# Created:     15/12/2013
# Copyright:   (c) Baig-Admin 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import tkinter.filedialog

# Accordking to MS Word, sowpods.txt has 267,751 words spread over 4959 pages!

class scrabble(object):
    def __init__(self, sowpods_filepath):
        self.fpath = sowpods_filepath

    def line_count(self):
        print("Hello world !!!  How are you ??? " + self.fpath + "\n")

# def scrabble():
#   read_sowpods()

def main():
    sowpods_filepath = tkinter.filedialog.askopenfilename()
    scr = scrabble(sowpods_filepath)
    scr.line_count()

if __name__ == '__main__':
    main()
=======
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     Write a Scrabble cheater
#
# Author:      Baig-Admin
#
# Created:     15/12/2013
# Copyright:   (c) Baig-Admin 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import tkinter.filedialog

# Accordking to MS Word, sowpods.txt has 267,751 words spread over 4959 pages!

class scrabble(object):
    def __init__(self, sowpods_filepath):
        self.fpath = sowpods_filepath

    def line_count(self):
        print("Hello world !!!  How are you ??? " + self.fpath + "\n")

# def scrabble():
#   read_sowpods()

def main():
    sowpods_filepath = tkinter.filedialog.askopenfilename()
    scr = scrabble(sowpods_filepath)
    scr.line_count()

if __name__ == '__main__':
    main()
>>>>>>> 3a3eeac04cbe757a5a977da746abe95ab991826d
