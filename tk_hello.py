<<<<<<< HEAD
#-------------------------------------------------------------------------------
# Name:        TkHello
# Purpose:
#
# Author:      Babar Baig
#
# Created:     23/06/2012
# Copyright:   (c) Baig-Daily 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

# I tried to encapsulate the code into a function and broke it. Label won't
# resize until I know enough about Python to fix issues with reszie() and scale()

from tkinter import *

def resize(eval=None):
    label.config(font='Helveetica -%d bold' % scale.get())

def Build_GUI():
    '''
    top = Tk()      # Root window
    hello = tkinter.Label(top, text='\nHello world!\n')
    hello.pack()
    quit = tkinter.Button(top, text='Quit', command=top.quit, bg='blue', fg='white')
    quit.pack(fill=tkinter.X, expand=1)
    '''
    top = Tk()
    top.geometry('250x150')

    label = Label(top, text='Hello World!', font='Helvetica -12 bold')
    label.pack(fill=Y, expand=1)

    scale = Scale(top, from_=10, to=40, orient=HORIZONTAL)
    scale.set(12)
    scale = Scale(top, from_=10, to=40, orient=HORIZONTAL,
        command=resize)
    scale.pack(fill=X, expand=1)

    quit = Button(top, text='Quit', command=top.quit, activeforeground='white',
        activebackground='red')
    quit.pack()

if __name__ == '__main__':
    Build_GUI()
    mainloop()
    # print('Hello, world!')
=======
#-------------------------------------------------------------------------------
# Name:        TkHello
# Purpose:
#
# Author:      Babar Baig
#
# Created:     23/06/2012
# Copyright:   (c) Baig-Daily 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

# I tried to encapsulate the code into a function and broke it. Label won't
# resize until I know enough about Python to fix issues with reszie() and scale()

from tkinter import *

def resize(eval=None):
    label.config(font='Helveetica -%d bold' % scale.get())

def Build_GUI():
    '''
    top = Tk()      # Root window
    hello = tkinter.Label(top, text='\nHello world!\n')
    hello.pack()
    quit = tkinter.Button(top, text='Quit', command=top.quit, bg='blue', fg='white')
    quit.pack(fill=tkinter.X, expand=1)
    '''
    top = Tk()
    top.geometry('250x150')

    label = Label(top, text='Hello World!', font='Helvetica -12 bold')
    label.pack(fill=Y, expand=1)

    scale = Scale(top, from_=10, to=40, orient=HORIZONTAL)
    scale.set(12)
    scale = Scale(top, from_=10, to=40, orient=HORIZONTAL,
        command=resize)
    scale.pack(fill=X, expand=1)

    quit = Button(top, text='Quit', command=top.quit, activeforeground='white',
        activebackground='red')
    quit.pack()

if __name__ == '__main__':
    Build_GUI()
    mainloop()
    # print('Hello, world!')
>>>>>>> 3a3eeac04cbe757a5a977da746abe95ab991826d
