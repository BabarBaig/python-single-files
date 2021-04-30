#-------------------------------------------------------------------------------
# Name:        approximate_size
# Purpose:
#
# Author:      Baig-Daily
#
# Created:     19/01/2012
# Copyright:   (c) Baig-Daily 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#!/usr/bin/env python

SUFFIXES = {1000:  ['KB' , 'MB' , 'GB' , 'TB' , 'PB' , 'EB' , 'ZB' , 'YB' ],
            1024:  ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

def approximate_size(size, a_kilobyte_is_1024_bytes=True):
        #Convert a file size to human-readable form
    if size  < 0:
        raise  ValueError('Number must  be non-negative')

    multiple = 1024  if a_kilobyte_is_1024_bytes else  1000
    for suffix  in SUFFIXES[multiple]:   #Iterate appropritate SUFFIXES[][]
        size  /= multiple
        if size  < multiple:        #Note the format string to format output
            return  '{0:.1f} {1}'.format(size, suffix)
    raise  ValueError('number too large')

if __name__  == '__main__':
    print(approximate_size(1000000000000))
    print(approximate_size(1000000000000, False))
    print(approximate_size(12345678))
    print(approximate_size(12345678, False))
