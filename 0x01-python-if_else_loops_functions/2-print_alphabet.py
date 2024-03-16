#!/usr/bin/python3
"""Prints ASCII alphabet, in lowercase, not followed by a new line"""

for alpha in range(97, 123):
    print("{}".format(chr(alpha)), end="")
