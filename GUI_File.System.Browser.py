#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Baig-Daily
#
# Created:     24/06/2012
# Copyright:   (c) Baig-Daily 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import os
from time import sleep
from tkinter import *

class DirList(object):
    def __init__(self, initdir=None):
        self.top = Tk()
        self.label = Label(self.top, text='Directory Lister v1.1')
        self.label.pack()

        self.cwd = StringVar(self.top)

        self.dirl = Label(self.top, fg='blue', font=('Helvetica', 12, 'bold'))
        self.dirl.pack()

        self.dirfm = Frame(self.top)
        self.dirsb = Scrollbar(self.dirfm)
        self.dirsb.pack(side=RIGHT, fill=Y)
        self.dirsb = Listbox(self.dirfm, height=15, width=50, yscrollcommand=self.dirsb.set)
        self.dirsb.bind('<Double-1>', self.setDirAndGo)
        self.dirsb.config(command=self.dirs.yview)
        self.dirsb.pack(side=LEFT, fill=BOTH)
        self.dirfm.pack()

        self.dirn = Entry(self.top(), width=50, textvariable=self.cwd)
        self.dirn.bind('<Return>', self.doLS)
        self.dirn.pack()

        self.bfm = Frame(self.top)
        self.clr = Button(self.bfm, text='Clear', command=self.clrDir,
            activeforegound='white', activebackground='blue')
        self.ls = Button(self.bfm, text='List Directory', command=self.doLS,
            activeforegound='white', activebackground='green')
        self.quit = Button(self.bfm, text='Quit', command=self.top.quit,
            activeforegound='white', activebackground='red')
        self.clr.pack( side=LEFT)
        self.ls.pack(  side=LEFT)
        self.quit.pack(side=LEFT)
        self.bfm.pack()

        if initdir:
            self.cwd.set(os.curdir)
            self.doLS()

def clrDir(self, eval=None):
    self.cwd.set('')

def setDirAndGo(self, eval=None):
    self.last = self.cwd.get()
    self.dirs.config(selectbackground='red')
    check = self.dirs.get(self.dirs.curselection())
    if not check:
        check = os.curdir
    self.cwd.self(check)
    self.doLS()

def doLS(self, eval=None):
    pass

def main():
    pass

if __name__ == '__main__':
    main()
