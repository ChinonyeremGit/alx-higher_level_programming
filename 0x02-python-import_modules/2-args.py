#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    ac = len(argv) - 1
    if ac == 0:
        print("{} arguments.".format(ac))
    elif ac == 1:
        print("{} argument:".format(ac))
        print("{}: {}".format(ac, argv[1]))
    else:
        print("{} arguments:".format(ac))
        for i, value in enumerate(argv):
            if i == 0:
                continue
            print("{}: {}".format(i, value))
