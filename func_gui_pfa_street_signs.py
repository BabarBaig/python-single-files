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

import functools
import tkinter
from tkinter.messagebox import showinfo, showwarning, showerror

def BuildStreetSignsGUI():
    WARN = 'warn'   # Warning
    CRIT = 'crit'   # Critical message
    REGU = 'regu'   # Regular message

    SIGNS = {
        'Do Not Enter':      CRIT,
        'Railroad Crossing': WARN,
        '65 Speed Limit':    REGU,
        'Wrong Way':         CRIT,
        'Merging Traffic':   WARN,
        'One Way':           REGU,
    }

    critCB = lambda: showerror(  'Error',     'Error Button Pressed')
    warnCB = lambda: showwarning('Warning', 'Warning Button Pressed')
    infoCB = lambda: showinfo(   'Info',       'Info Button Pressed')

    top = tkinter.Tk()
    top.title('Road Signs')
    quit = tkinter.Button(top, text='QUIT', command=top.quit, bg='red', fg='white')
    quit.pack()

    MyButton   = functools.partial(tkinter.Button, top)
    CritButton = functools.partial(MyButton, command=critCB, bg='white', fg='red')
    WarnButton = functools.partial(MyButton, command=warnCB, bg='goldenrod1')
    ReguButton = functools.partial(MyButton, command=infoCB, bg='white')

    for eachSign in SIGNS:
        signType = SIGNS[eachSign]
        cmd = '%sButton(text=%r%s).pack(fill=X, expand=True)' % (
            signType.title(), eachSign, '.upper()' if signType==CRIT
            else '.title()')
        eval(cmd)

BuildStreetSignsGUI()
mainloop()
