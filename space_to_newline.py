
import os

def space_to_newline():
    """ Convert spaces in a file to newlines, so you end-up with one word/line """

    os.chdir(r"C:\000\02_LR\LR Python")
    read_file  = open("space to newline_rdonly.txt")
    write_file = open("space to newline_wronly.txt",'w')
    for read_line in read_file:
        write_file.write(read_line.translate({ord(c): '\n' for c in " "}))
        # print(read_line)
    read_file.close()
    write_file.close()
"""        print('Rename '    + file_name +
              '  to: '     + file_name.translate({ord(c): None for c in "0123456789"}))
        os.rename(file_name, file_name.translate({ord(c): None for c in "0123456789"}))
"""

space_to_newline()
