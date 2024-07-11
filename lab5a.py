#!/usr/bin/env python3
# Author ID: cklau9

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    f = open(file_name, 'r')
    contents = f.read()
    f.close()
    return contents


def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters
    f = open(file_name, 'r')
    read_data = f.read()
    f.close()
    read_data.split('\n') # Returns a list but it need further remove the last empty string
    list_of_lines = read_data.split('\n') # name the returned list object as list_of_lines

    no_empty_lines = [] # Create an empty list nonempty_lines to save non-empty lines from read_data.split('\n)
    # Iterate over each line in the list of lines
    for line in list_of_lines:
        if line != '': 
            no_empty_lines.append(line) # Add the no-empty line to the stipped_lines list
    return no_empty_lines


if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))