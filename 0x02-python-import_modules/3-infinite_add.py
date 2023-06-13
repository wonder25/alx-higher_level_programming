#!/usr/bin/python3

import sys

sum_all = 0
if __name__ == '__main__':
    for args in sys.argv[1:]:
        sum_all += int(args)

    print("{:d}".format(sum_all))
