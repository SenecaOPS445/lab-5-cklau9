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

def append_file_string(file_name, string_of_lines):
    # Takes two strings, appends the string to the end of the file
    f = open(file_name, 'a')
    f.write(string_of_lines)
    f.close()

def write_file_list(file_name, list_of_lines):
    # Takes a string and list, writes all items from list to file where each item is one line
    f = open(file_name, 'w')
    for items in list_of_lines:
        f.write(items + '\n')
    f.close()

def copy_file_add_line_numbers(file_name_read, file_name_write):
    # Takes two strings, reads data from first file, writes data to new file, adds line number to new file
    file_read = open(file_name_read, 'r')
    data = file_read.readlines()
    file_read.close()

    file_write = open(file_name_write, "w")
    counter = 1
    for line in data:
        line_with_number = str(counter) + ':' + line
        file_write.write(line_with_number)
        counter += 1
    file_write.close()
                
if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))