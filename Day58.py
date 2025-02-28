#!/bin/python3

import math
import os
import random
import re
import sys
def designerPdfViewer(h, word):
    max_height = 0
    for char in word:
        index = ord(char) - ord('a')
        max_height = max(max_height, h[index])
        area = max_height * len(word)
    
    return area
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
