#!/usr/bin/python3
for number in range(0, 99):
    result = chr(number)
    result = hex(ord(result))
    print("{} = {}".format(number, result))
