#!/usr/bin/python3
"""
Module 1-write_file

contains write_file function
which writes a string  to a text file and return number of character written
"""


def write_file(filename="", text=""):
    """
     write string to textfile
     Args:
      filename (str): filename
      text (str): string to be wriiten to a textfile
     Return:
       return number of character written on a file
    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
