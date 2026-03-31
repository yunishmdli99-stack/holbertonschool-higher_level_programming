#!/usr/bin/python3
for i in range(26):
    if (i == 4 or i == 16):
        pass
    else:
        print("{}".format(chr(i + 97)), end="")
