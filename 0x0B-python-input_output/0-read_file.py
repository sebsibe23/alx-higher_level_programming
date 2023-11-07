#!/usr/bin/python3


def read_file(filename=""):
    """
    Function Name: read_file
    Parameters: filename (str): The name of the file to be read.
    Default is an empty string.
    Description: This function reads a text file (UTF8) and
    prints it to stdout.
    It opens the file with the given filename in read mode with UTF-8 encoding,
    then reads the file content and prints it to stdout. The 'with' statement
    is used to handle the file open/close operations.
    This function doesn't handle file permission or
    file doesn't exist exceptions.
    """
    with open(filename, 'r', encoding='utf-8') as varfilename:
        print(varfilename.read())
