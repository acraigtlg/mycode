#! usr/bin/env python3

foo= open("dracula.txt", "r")
foo.close()


for line in foo:
    if "vampire" in line.lower():
        print(line)
