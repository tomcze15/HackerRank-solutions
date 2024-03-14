#!/bin/python3

import math
import os
import random
import re
import sys


def isodd(number):
    return n % 2 != 0


if __name__ == '__main__':
    n = int(input().strip())

    if isodd(n):
        print("Weird")

    if not isodd(n) and 2 <= n <= 5:
        print("Not Weird")

    if not isodd(n) and 6 <= n <= 20:
        print("Weird")

    if not isodd(n) and 20 < n:
        print("Not Weird")
