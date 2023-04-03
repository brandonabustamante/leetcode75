"""
/********************************************************************************
    Given two strings s and t, return true if s is a subsequence of t, or false
    otherwise.

    A subsequence of a string is a new string that is formed from the original
    string by deleting some (can be none) of the characters without disturbing
    the relative positions of the remaining characters. (i.e., "ace" is a
    subsequence of "abcde" while "aec" is not).

    Example 1:
    Input: s = "abc", t = "ahbgdc"
    Output: true

    Example 2:
    Input: s = "axc", t = "ahbgdc"
    Output: false

*********************************************************************************/
"""

def isSubsequence(s, t):

    iter_s = 0
    iter_t = 0
    len_s = len(s)
    len_t = len(t)

    while (iter_s < len_s) and (iter_t < len_t):

        if s[iter_s] == t[iter_t]:
            iter_s += 1

        iter_t += 1

    return iter_s == len_s


def main():
    s = "abc"
    t = "ahbgd"
    print(isSubsequence(s, t))


if __name__ == "__main__":
    main()
