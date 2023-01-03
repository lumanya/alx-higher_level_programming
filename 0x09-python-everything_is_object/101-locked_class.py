#!/usr/bin/python3
"""
101-locked_clas module
with no clas or objects attribute, that prevents user createing instance
attribute except if attribute is first_name
"""


class LockedClass:
    """
    prevent user from creating new instances attribute dynamically
    unless attribute is "firstname
    """

    __slots__ = "first_name"
