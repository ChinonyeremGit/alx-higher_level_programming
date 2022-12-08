#!/usr/bin/python3
if __name__ == "__main__":
    from random import choice
    my_list = ["H", "T"]
    new_list = []
    for i in range(101):
        new_list.append(choice(my_list))
    print("Heads :", new_list.count("H"))
    print("Tails :", new_list.count("T"))
