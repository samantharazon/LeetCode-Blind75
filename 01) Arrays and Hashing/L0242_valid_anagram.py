def validAnagram(s: str, t: str):

    if len(s) != len(t):
        return False

    countS = {}
    countT = {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0) 
        countT[t[i]] = 1 + countT.get(t[i], 0) 
    
    for c in countS:
        if countS[c] != countT.get(c, 0): 
            return False

    return True



word1 = "anagram"
word2 = "nagaram"

print(validAnagram(word1, word2))

word1 = "helloo"
word2 = "ollehh"

print(validAnagram(word1, word2))