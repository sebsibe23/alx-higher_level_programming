#!/usr/bin/python3
for charletter in range(97, 123):
    if chr(charletter) is not 'q' and chr(charletter) is not 'e':
        print("{}".format(chr(charletter)), end="")
