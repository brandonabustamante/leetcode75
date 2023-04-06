
def longestPalindrome(s):

    letters = {}
    palindrom_len = 0
    single_letter_flag = 0

    for letter in s:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

    for letter in letters:
        if letters[letter] % 2 == 0:
            palindrom_len += letters[letter]
            letters[letter] = 0

        if letters[letter] > 2:
            palindrom_len += (letters[letter] - 1)
            letters[letter] = 1


        if letters[letter] == 1 and single_letter_flag == 0:
            single_letter_flag = 1
            palindrom_len += 1
            
    return palindrom_len

def main():
    #s = "abccccdd"
    s = "ccc"
    print(longestPalindrome(s))


if __name__ == "__main__":
    main()
