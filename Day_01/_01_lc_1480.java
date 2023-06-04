import java.util.Arrays;

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
public class _01_lc_1480 {
    
    public static int[] runningSum(int[] nums) {

        int ARRSIZE = nums.length;
        int runSum = 0;
        int[] sumNums = new int[ARRSIZE];
        int idx = 0;

        for (int num : nums) {
            runSum += num;
            sumNums[idx] = runSum;
            idx++;
        }

        return sumNums;

    }
    public static void main(String[] args) {
        // Test Cases
        int[] test_1 = {1, 2, 3, 4};
        int[] test_2 = {1, 1, 1, 1, 1};
        int[] test_3 = {3, 1, 2, 10, 1};
    
        System.out.println(Arrays.toString(runningSum(test_1)));
        System.out.println(Arrays.toString(runningSum(test_2)));
        System.out.println(Arrays.toString(runningSum(test_3)));

    }

}
