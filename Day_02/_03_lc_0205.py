"""*****************************************************************************
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get
t.

All occurrences of a character must be replaced with another character while
preserving the order of characters. No two characters may map to the same 
character, but a character may map to itself.
 
Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true
 

Constraints:
1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.

Solution:
1.Declare two maps s to t and t to s
2.Iterate over both strings concurrently
3.Initialize the current s and t characters into two variables
4.Check if the s character mapping exists in the s maps to t map
	If the s maps to t map at s character do not equal the t
	character, return False
5.Otherwise
	If the t character mapping exists in t maps to s
		Return False
6.Add the mapping in s maps to t at s character to point to the t character
7.Add the mapping in the t maps to s at t character to point the the s character
8.If the loop completes, return True


*****************************************************************************"""

def isIsomorphic(s, t):
    s_maps_to_t = {}
    t_maps_to_s = {}

    SIZE = len(s)

    for i in range(SIZE):
        s_char = s[i]
        t_char = t[i]

        if s_char in s_maps_to_t:
            if s_maps_to_t[s_char] != t_char:
                return False
        else:
            if t_char in t_maps_to_s:
                return False                      
        
        s_maps_to_t[s_char] = t_char
        t_maps_to_s[t_char] = s_char
    
    return True

def main():
    s_1 = 'egg'
    t_1 = 'add'

    s_2 = 'foo'
    t_2 = 'bar'

    s_3 = 'paper'
    t_3 = 'title'

    print(isIsomorphic(s_1, t_1))
    print(isIsomorphic(s_2, t_2))
    print(isIsomorphic(s_3, t_3))

if __name__ == "__main__":
    main()