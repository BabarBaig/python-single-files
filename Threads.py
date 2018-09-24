#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        Concurrent.Futures.py
# Purpose:
#
# Author:      Babar Baig
#
# Created:     06/18/2012
# Copyright:   (c) Baig-Daily 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#from os import getcwd
#from shutil import move
#from concurrent.futures import ProcessPoolExecutor
#from time import ctime, sleep
#from concurrent.futures import ThreadPoolExecutor
import concurrent.futures

def Loop(loop_count):
    print("Starting loop", loop_count,"at:", ctime())
    sleep(2)
    print("Ending   loop", loop_count,"at:", ctime())

def main():
    with ThreadPoolExecutor(max_workers=4) as e:
        future = e.submit(Loop, 1)
        future = e.submit(Loop, 2)
        future = e.submit(Loop, 3)
        future = e.submit(Loop, 4)
        print(future.result())

if __name__ == '__main__':
    main()
