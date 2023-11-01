#!/usr/bin/python3
"""Module for text formatting"""
def text_indentation(text):
    """Function to add two new lines after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        text = text.replace('.', '.\n\n')
        text = text.replace('?', '?\n\n')
        text = text.replace(':', ':\n\n')
        print('\n'.join([line.strip() for line in text.split('\n')]), end='')

