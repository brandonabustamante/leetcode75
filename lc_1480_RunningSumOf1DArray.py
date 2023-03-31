"""
/********************************************************************************
    Given an array nums. We define a running sum of an array as
    runningSum[i] = sum(nums[0]…nums[i]).

    Return the running sum of nums.

    Example 1:

    Input: nums = [1,2,3,4]
    Output: [1,3,6,10]
    Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

*********************************************************************************/
"""

def runningSum(nums):
    new_nums = []
    runningTotal = 0

    for element in nums:
        runningTotal += element
        new_nums.append(runningTotal)

    return new_nums

def main():
    nums = [1, 2, 3, 4]
    nums = runningSum(nums)

    for element in nums:
        print(element, end=" ")

    print()
if __name__ == "__main__":
    main()

