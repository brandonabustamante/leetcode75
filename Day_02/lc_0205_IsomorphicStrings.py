"""
/********************************************************************************
    Given two strings s and t, determine if they are isomorphic.
    Two strings s and t are isomorphic if the characters in s can be replaced to
    get t.
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
*********************************************************************************/
"""
def isIsomorphic(s, t):

    s_letters = {}
    t_letters = {}
    
    for char_s, char_t in zip(s, t):   
        if char_s not in s_letters:
            s_letters[char_s] = char_t
        else:
            if s_letters[char_s] != char_t:
                return False

        if char_t not in t_letters:
            t_letters[char_t] = char_s
        else:
            if t_letters[char_t] != char_s:
                return False

    return True


def main():
    s = "egg"
    t = "add"
    print(isIsomorphic(s, t))

if __name__ == "__main__":
    main()
