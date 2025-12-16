#https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem

#1. Time Limit 2. O(N^2)

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    from itertools import combinations
    # Write your code here
    min_val = float("inf")
    
    for x,y in (combinations(arr,2)):
        min_val = min(min_val, abs(x+(-1)*y), abs(y+(-1)*x))
    return min_val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()


#2. O(N)
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    from itertools import combinations
    # Write your code here
    min_val = float("inf")
    arr.sort()
    for i in range(len(arr)-1):
        min_val = min(min_val, abs(arr[i]-arr[i+1]), abs(arr[i+1]-arr[i]))
    return min_val  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
