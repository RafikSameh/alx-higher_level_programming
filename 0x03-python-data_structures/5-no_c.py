#!/usr/bin/python3
def no_c(my_string):
    new = [x for x in my_string]
    new.remove('c')
    new.remove('C')
    return (new)
