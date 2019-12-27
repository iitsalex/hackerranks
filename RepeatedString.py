#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
'''
def repeatedString(s, n):
    my_str = ""
    repeatedStrings = math.ceil(n/len(s))
    my_str = s*repeatedStrings
    new_str = my_str[0:n]
    count = new_str.count('a')
    return count

'''

def repeatedString(s, n):
    return (s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
