/********************************************************************************
    Given an array nums. We define a running sum of an array as
    runningSum[i] = sum(nums[0]…nums[i]).

    Return the running sum of nums.

    Example 1:

    Input: nums = [1,2,3,4]
    Output: [1,3,6,10]
    Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

*********************************************************************************/

public class lc_1480_RunningSumOf1DArray {

    public static int[] runningSum(int[] nums) {

        int size = nums.length;
        int[] newNums = new int[size];
        int runningTotal = 0;

        for (int i = 0; i < size; i++) {
            runningTotal += nums[i];
            newNums[i] = runningTotal;
        }

        return newNums;
    }

    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 4};
        nums = runningSum(nums);
        
        for (int element : nums) {
            System.out.print(element + " ");
        }
        System.out.println();
    }
}
