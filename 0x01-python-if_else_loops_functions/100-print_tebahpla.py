#!/usr/bin/python3
c = 0
for i in range(26):
    print("{:s}" .format(chr(122 - i))
            if i % 2 == 0
            else
                "{:s}".format(chr(90 - i)), end="")
