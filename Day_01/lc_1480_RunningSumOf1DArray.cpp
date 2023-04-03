/********************************************************************************
    Given an array nums. We define a running sum of an array as
    runningSum[i] = sum(nums[0]…nums[i]).

    Return the running sum of nums.

    Example 1:

    Input: nums = [1,2,3,4]
    Output: [1,3,6,10]
    Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

*********************************************************************************/

#include <iostream>
#include <vector>

using namespace std;

vector<int> runningSum(vector<int> &nums)
{
    vector<int> newNums;
    int runningTotal = 0;

    for (const auto element : nums)
    {
        runningTotal += element;
        newNums.push_back(runningTotal);
    }

    return newNums;
}

int main()
{
    vector<int> nums{1, 2, 3, 4};
    nums = runningSum(nums);
    
    for (const auto element : nums)
    {
        cout << element << " ";
    }
    cout << endl;
}