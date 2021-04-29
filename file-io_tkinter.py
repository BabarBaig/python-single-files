
# Use tkinter to browse to a folder and open a text log file readonly
# Read 1st 10 lines, strip extra newline => print line read
# Read 6 fields from each line => print the 6 fields

import sys
import tkinter.filedialog

def main():
    read_file = tkinter.filedialog.askopenfilename()
    print(read_file)
    with open(read_file, 'r') as fp:
        counter = 0
        for line in fp:
            print( line.strip('\n'))
            data = line.strip().split('\t')
            print(len(data), data)
            counter += 1
            if counter >= 15:
                break

if __name__ == '__main__':
    main()
