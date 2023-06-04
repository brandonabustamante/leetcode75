#include <iostream>
#include <vector>
/*******************************************************************************
    Given an array nums. We define a running sum of an array as
    runningSum[i] = sum(nums[0]…nums[i]).

    Return the running sum of nums.

    Example 1:
    Input: nums = [1,2,3,4]
    Output: [1,3,6,10]
    Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

    Example 2:
    Input: nums = [1,1,1,1,1]
    Output: [1,2,3,4,5]
    Explanation: Running sum is obtained as follows:
    [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

    Example 3:
    Input: nums = [3,1,2,10,1]
    Output: [3,4,6,16,17]

    Constraints:

    1 <= nums.length <= 1000
    -10^6 <= nums[i] <= 10^6

    Solution:

    1.Declare a variable to track the running sum
    2.Declare a new array to place the running sum values
    3.Iterate over the original array
    4.Add the current number from the original array to the running sum
    5.Append the current running sum to the new array
    6.Loop until the end of the original array is reached
    7.Return the new array

*******************************************************************************/

std::vector<int> runningSum(std::vector<int> &nums)
{
    int runSum = 0;
    std::vector<int> sumNums;

    for (int num : nums)
    {
        runSum += num;
        sumNums.push_back(runSum);
    }

    return sumNums;
}

void printVector(std::vector<int> &nums)
{
    for (int num : nums)
    {
        std::cout << num << " ";
    }
    std::cout << "\n";
    return;
}

int main()
{
    std::vector<int> test_1 = {1, 2, 3, 4};
    std::vector<int> test_2 = {1, 1, 1, 1, 1};
    std::vector<int> test_3 = {3, 1, 2, 10, 1};

    test_1 = runningSum(test_1);
    test_2 = runningSum(test_2);
    test_3 = runningSum(test_3);

    printVector(test_1);
    printVector(test_2);
    printVector(test_3);

    return 0;
}