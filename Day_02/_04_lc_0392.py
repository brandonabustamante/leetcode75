"""*****************************************************************************
Given two strings s and t, return true if s is a subsequence of t, or false
otherwise.

A subsequence of a string is a new string that is formed from the original 
string by deleting some (can be none) of the characters without disturbing the 
relative positions of the remaining characters. (i.e., "ace" is a subsequence of
"abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
 
Constraints:
0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.

Solution:
1.Initialize two variables to the lengths of the two strings
2.Initialize two variables for the strings' indexes
3.Loop over both strings concurrently until the end of either is reached
4.Check if the current characters are equal
	Increment the s index
5.Increment the t index
6.Once the loop is complete, check if the s index equals the length of s
	Return True
7.Otherwise
	Return False
*****************************************************************************"""

def isSubsequence(s, t):
    LEN_S = len(s)
    LEN_T = len(t)   
    s_idx = 0
    t_idx = 0

    while s_idx < LEN_S and t_idx < LEN_T:
        if s[s_idx] == t[t_idx]:
            s_idx += 1
        
        t_idx += 1
    
    if s_idx == LEN_S:
        return True
    return False

def main():
    s_1 = "abc" 
    t_1 = "ahbgdc"
    s_2 = "axc" 
    t_2 = "ahbgdc"

    print(isSubsequence(s_1, t_1))
    print(isSubsequence(s_2, t_2))


if __name__ == "__main__":
    main()