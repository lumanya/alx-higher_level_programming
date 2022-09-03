#!/usr/bin/python3
new = []


def search_replace(my_list, search, replace):
    if my_list is not None:
        for i in my_list:
            if i == search:
                new.append(replace)
            else:
                new.append(i)
        return new
    else:
        return None
