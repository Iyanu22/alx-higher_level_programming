#!/usr/bin/python3
for num1 in range(0, 8):
    for num2 in range(0, 10):
        if num1 != num2:
            if num1 < num2:
                print("{}{}, ".format(num1, num2), end='')
print("{}{}".format(num1 + 1, num2))
print()
