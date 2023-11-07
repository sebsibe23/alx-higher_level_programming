#!/usr/bin/python3


def append_write(filename="", text=""):
    """
    Function to append a given text into a file.
    Parameters:
    filename (str): The name of the file to append to.
    If the file does not exist, it will be created.
    text (str): The text to append into the file.
    Returns:
    int: The number of characters appended into the file.
    """
    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
