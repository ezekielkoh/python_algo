"""
Kadane's Algorithm

Function: To identify maximum subarray sum in a given array
Input: Array of integers
Output: Maximum subarray sum
"""

def maxSubarraySum(arr):
    maxValue = float('-inf')
    currValue = 0
    subarr = [] # holds value of subarray with max sum

    for i in range(len(arr)):
        currValue += arr[i]

        if currValue > maxValue:
            maxValue = currValue
    
        elif currValue < 0:
            currValue = 0
            subarr.clear()

    return maxValue