#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""
Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...
Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().
"""

import sys
import operator

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

def build_word_count_dict(data_file):
    print("Opening {0}".format(data_file))  # Note Python 3 style formatting
    f = open(data_file, "r")            # 'a' append, 'r' read, 'rU' smart \n, 'w' write
    data_string = f.read()              # read entire data_file into a string
    data_array = data_string.split()    # Split text into words on *all* whitespace
    data_dict = {}
    for word in data_array:
        word_lower = word.lower()
        if word_lower in data_dict:
            data_dict[word_lower] += 1
        else:
            data_dict[word_lower] = 1
    f.close()
    return data_dict

def print_words(data_file):
    data_dict = build_word_count_dict(data_file)
    for key in sorted(data_dict):
        print('{0:20s} {1:2d}'.format(data_dict[key], key))

def print_top(data_file):
    data_dict = build_word_count_dict(data_file)    # data_dict is inherently unsorted
    sorted_list = sorted(data_dict.items(), key=lambda x: x[1], reverse=True)
#   print(sorted_list)  # Print *entire* sorted list of word/freq tuples
    counter = 0
    max_count = 20
    for cur_tuple in sorted_list:   # Exits gracefully if len(sorted_list) < max_count
        if counter == max_count:    break
        else:                       counter += 1
        print('{0:s} {1:d}'.format(cur_tuple[0], cur_tuple[1]))
#       print(cur_tuple)    # Messy looking bunch of [(str1,freq1),(str2,freq2),...]
#       print('{0:20s} {1:2d}'.format(cur_tuple[0], cur_tuple[1]))

# ==============================================
# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    if len(sys.argv) != 3:
        print('usage: ./wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)

if __name__ == '__main__':
  main()
