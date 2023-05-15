
from collections import defaultdict

def groupAnagrams (strs: list[str]):
    # create a hashmap
    res = defaultdict(list) # mapping charCount to list of Anagrams
    
    for word in strs:
        # create an array
        count = [0] * 26 # making 26 zero's because a...z has 26 letters

        # create a count for each word
        for letter in word:
            # map each character to the appropriate index
            count[ord(letter) - ord("a")] += 1 # add a 1 to the right location of the 26 zero's
                                          # this is counting what letters appear & how many of them
                                          # (EX) a = 65 ---> 65 - 65 = 0
                                          # (EX) b = 66 ---> 66 - 65 = 1
                                          # count[0] = count[0] + 1
                                          
        # create key-value pair [count, words]
        res[tuple (count)].append(word) # in res, find where key (count) appears & append value s (the word) to end of list

    return res.values()
    

strs = ["eat","tea","tan","ate","nat","bat"]
result = groupAnagrams(strs)
print("\n")
print(result) 
print("\n")