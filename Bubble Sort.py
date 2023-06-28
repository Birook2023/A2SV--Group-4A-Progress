#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    sorted = False
    swaps = 0
    
    while not sorted:
        sorted = True
        
        for i in range(len(a)-1):
            if a[i] > a[i +1]:
                a[i], a[i+1] = a[i+1], a[i]
                swaps +=1
                sorted = False
    
    print("Array is sorted in",swaps, "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[len(a)-1])
    return a

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
