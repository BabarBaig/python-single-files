
import os

def convert_to_newline(replchar):
    """ Find replchar in a file and convert it to newlines """

    os.chdir(r"C:\000\01_proj\Python_crs_Udacity_PFP")
    read_file  = open("path_semicolon.txt")
    write_file = open("path_newline.txt",'w')
    for read_line in read_file:
        print(read_line)
        write_file.write(read_line.translate({ord(c): '\n' for c in replchar}))
    read_file.close()
    write_file.close()
"""        print('Rename '    + file_name +
              '  to: '     + file_name.translate({ord(c): None for c in "0123456789"}))
        os.rename(file_name, file_name.translate({ord(c): None for c in "0123456789"}))
"""

convert_to_newline(';')
