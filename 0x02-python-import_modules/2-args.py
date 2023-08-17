#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = len(argv) - 1

    if i == 0:
        print("0 arguments.")
    elif i == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(i))
    for index in range(i):
        print("{}: {}".format(index + 1, argv[index + 1]))
