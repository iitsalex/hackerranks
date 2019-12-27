#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the compute_number_score function below.

# 5 points for 7 in number

# 6 points for each pair of 2's, more than two 2's +6 per 2 XX

# n^2 points for a sequence of n >= 1 where each digit is descending <

# 4 points if the entire number is a multiple of 3 XX

# 3 points for even digits XX

def compute_number_score(number):
    pointsCounter = 0
    pairBool = False
    prevDigit = -1
    consecCount = 1
    lst = [int(c) for c in str(number)]
    if number % 3 == 0:
        pointsCounter += 4
    for digit in lst:
        if digit % 2 == 0:
            pointsCounter += 3
        if digit == 7:
            pointsCounter += 5
        if pairBool and digit == 2:
            pointsCounter += 6
        elif digit == 2 and prevDigit == 2:
            pairBool = True
            pointsCounter += 6
        else:
            pairBool = False
        if digit == prevDigit - 1:
            consecCount += 1
        else:
            pointsCounter += consecCount ** 2
            consecCount = 1
        prevDigit = digit

    return pointsCounter


if __name__ == '__main__':
    print(compute_number_score(321))
