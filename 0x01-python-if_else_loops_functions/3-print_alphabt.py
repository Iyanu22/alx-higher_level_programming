#!/usr/bin/python3
for number in range(ord('a'), ord('z') + 1):
    if chr(number) != 'q' and chr(number) != 'e':
        print('{:c}'.format(number), end='')
