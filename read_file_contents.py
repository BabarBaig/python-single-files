import os

def read_file_contents(base_dir, read_file):
    ''' This can be used as a helper function to read contents of a file
    '''
    os.chdir(base_dir)
    # print(os.listdir())
    file_handle = open(read_file)
    file_in_memory = file_handle.read()    # Read entire file into memory
    file_handle.close()
    print(file_in_memory)

read_file_contents(r'C:\000\01_proj\p_Python_IDLE', 'read_file_contents_data.txt')
