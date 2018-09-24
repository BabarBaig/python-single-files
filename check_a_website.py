import os
import urllib.request

''' In this sample file:
~ Read some data from a text file
~ Pass it to a website to check for profanities
~ Print website response (true/false) for any profanities
'''

def check_profanity():
    file_in_memory2 = read_file_contents(r'C:\000\01_proj\p_Python_IDLE', 'read_file_contents_data.txt')
    # print(file_in_memory2)
    output2 = check_a_website('http://www.wdyl.com/profanity?q=', file_in_memory2)
    output_str = str(output2)
    if "true" in output_str:
        print('Profamity alret!')
    elif "false" in output_str:
        print('No curse words found in this document')
    else:
        print('Couldn\'t scan the document properly')

def check_a_website(url_string, data):
    ''' HELPER: Send url_string + data (converted to text) to a website and return its
    response.
    '''
    connection = urllib.request.urlopen(url_string + urllib.parse.quote(data))
    return connection.read()

def read_file_contents(base_dir, read_file):
    ''' HELPER: Read contents of a file into a list and return list
    '''
    os.chdir(base_dir)
    # print(os.listdir())
    file_handle = open(read_file)
    file_in_memory = file_handle.read()    # Read entire file into memory
    file_handle.close()
    return file_in_memory

check_profanity()
