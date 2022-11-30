#!/usr/bin/python3
def uppercase(str):
    upper_string = ""
    for char in str:
        if ord(char) >= 97 and ord(char) <= 123:
            upper_string += chr(ord(char) - 32)
        else:
            upper_string += char
    print("{}".format(upper_string))
