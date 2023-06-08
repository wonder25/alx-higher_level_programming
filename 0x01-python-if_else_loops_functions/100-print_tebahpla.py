#!/usr/bin/python3
c = 0
for i in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(i - c)), end="")
    c = 32 if i == 0 else 0
