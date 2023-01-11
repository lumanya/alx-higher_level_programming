#!/usr/bin/python3
"""
Module 2-append_write

contains append_write functions
which appends a string at the end of the text file  and returns the number of
character
"""


def append_write(filename="", text=""):
    """
    append a string at the end of a text file and returns the number of
    character

    Args:
     filename (str): filename
     text (str): string written to a filename
    Return:
      return number of character written on file
    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
