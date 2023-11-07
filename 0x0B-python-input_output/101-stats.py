#!/usr/bin/python3
"""
This module reads lines from the standard input, parses them,
and keeps track of the total file size and the count of different status codes.

Variables:
    file_size (int): The total size of all files processed.
    status_tally (dict): A dictionary where the keys are
    status codes and the values are their counts.

Exceptions:
    KeyboardInterrupt: An exception that is raised when the user
    interrupts program execution, usually by pressing Ctrl+c.
"""


import sys

file_size = 0
status_tally = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
g = 0
try:
    for line in sys.stdin:
        tokens = line.split()
        if len(tokens) >= 2:
            a = g
            if tokens[-2] in status_tally:
                status_tally[tokens[-2]] += 1
                g += 1
            try:
                file_size += int(tokens[-1])
                if a == g:
                    g += 1
            except Exception:
                if a == g:
                    continue
        if g % 10 == 0:
            print("File size: {:d}".format(file_size))
            for varkey, value in sorted(status_tally.items()):
                if value:
                    print("{:s}: {:d}".format(varkey, value))
    print("File size: {:d}".format(file_size))
    for varkey, value in sorted(status_tally.items()):
        if value:
            print("{:s}: {:d}".format(varkey, value))

except KeyboardInterrupt:
    print("File size: {:d}".format(file_size))
    for varkey, value in sorted(status_tally.items()):
        if value:
            print("{:s}: {:d}".format(varkey, value))
