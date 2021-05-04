
#!/usr/bin/env python

# Run command 'tasklist /nh' to get a list of running tasks in Windows.
# Capture the output from stdout and strip WS (White Space) using RE (Regular
# Expressions)

import os
import re                   #Import the std lib re (Regular Expression) module

def foo():
    try:                    #Open data file data.txt in readonly mode
#       f = open('C:/Users/Baig-Daily/Documents/05.Learn/Python/blah.txt','r');
        f = os.popen('tasklist /nh', 'r')
    except IOError as e:
        print("File open error: ", e);
        return;
    for eachLine in f:      #Read data one line at a time into eachLine[]
#       print (re.split(r'\s\s+', eachLine.strip()))
#       print (re.split(r'\s\s+|\t', eachLine.strip()))
        print (re.split(r'\s\s+|\t', eachLine.strip()))
    f.close();          #Good practice, but not necessary

foo();

