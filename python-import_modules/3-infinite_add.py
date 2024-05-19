#!/usr/bin/python3
import sys

if __name__ == "__main__":
    result = 0
    for i in range(1, len(sys.argv)):
        s = int(sys.argv[i])
        result += s
    print(result)
