#!/usr/bin/python3
import sys

def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

if len(sys.argv) < 2 or not sys.argv[1].isdigit():
    print("Please give a valid integer.")
    sys.exit(1)

f = factorial(int(sys.argv[1]))
print(f)