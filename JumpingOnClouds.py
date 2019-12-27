#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.

def jumpingOnClouds(c):
    i = 0
    jumps = 0
    while True:
        if (i+2 < len(c) and c[i+2] == 0):
            i+=2
        elif (i + 1 < len(c)):
            i+=1
        else:
            break
        jumps+=1

    return jumps
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
