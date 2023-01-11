#!/usr/bin/python3
"""
Module 0-read_file

contains read_file
that read a textfile in utf and prints it to stdout
"""


def read_file(filename=""):
    """
    Read file and print its contets to stdout
    Args:
      filename (str): name of a text file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f.read():
            print(line, end="")
