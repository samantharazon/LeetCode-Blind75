def validAnagram(s: str, t: str):

    # If not same length they are not Anagrams
    if len(s) != len(t):
        return False

    # Creating dictionary to track letter(key) : size(value) 
    # Example: {'a' : 3}
    countS = {}
    countT = {}

    for i in range(len(s)):

        countS[s[i]] = 1 + countS.get(s[i], 0)  # increment count value by adding 1. 
                                                # why use get method? if character (key) doesn't exist, intialize to 0.
        countT[t[i]] = 1 + countT.get(t[i], 0)
    
    for c in countS:
        if countS[c] != countT.get(c, 0): # why use get? if character (key) exists in S but not C, initialize to 0 in C
            return False

    return True



word1 = "anagram"
word2 = "nagaram"

print(validAnagram(word1, word2))