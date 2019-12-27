#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countingValleys function below.

def split(word):
    return [char for char in word]


def counting_valleys(n, s):
    elevation = 0
    valleys = 0
    arr = split(s)
    # return arr
    for move in arr:
        if move == 'D':
            elevation -= 1
        elif move == 'U':
            elevation += 1
            if (elevation == 0):
                valleys += 1

    return valleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = counting_valleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
