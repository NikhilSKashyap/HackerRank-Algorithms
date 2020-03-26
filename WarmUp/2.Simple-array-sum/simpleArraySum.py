#!/bin/python3

import numpy as np

def simpleArraySum(ar):
    return ar.sum()

if __name__ == '__main__':
    arr = np.array([2,3,1,10])
    print(simpleArraySum(arr))