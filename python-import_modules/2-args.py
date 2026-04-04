#!/usr/bin/python3
from sys import argv
if __name__ == "__name__":
    argc = len(argv) - 1
    if argc == 1:
        print("{} argument:".format(argc))
    elif argc == 0:
        print("{} arguments.".format(argc))
    else:
        print("{} arguments:".format(argc))
    i = 1
    while i < len(argv):
        print("{}: {}".format(i, argv[i]))
        i += 1
