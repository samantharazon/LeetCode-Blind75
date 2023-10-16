from collections import defaultdict

def groupAnagrams (strs: list[str]):
                            # defaultdict(list) means "Defining a dictionary with values as a list"
    res = defaultdict(list) # {0 1 0 1: eat, tea, ate}  
                            # {0 0 0 1: nat, tan}
    
    for word in strs:
        count = [0] * 26 # create an array: making 26 zero's --> a...z has 26 letters
                         # 0 0 0 0 0 ....

        for letter in word: 
            count[ord(letter) - ord("a")] += 1  # map 'a' to index 0... map 'z' to index 25.
                                                # add a 1 to the value (how many times it appears)
                                                # (Ex) a) 65 - 65 = 0  (map 'a' to index 0)
                                                # (Ex) b) 66 - 65 = 1  (map 'b' to index 1)
                                                # (Ex) z) 90 - 65 = 25 (map 'z' to index 25)
                                                # find index of current letter & add 1 to value
                                                # 0 1 0 0 1 0
                                             
                                        # create key-value pair [count, words]  [0 0 1 0 0 1: eat]
        res[tuple (count)].append(word) # in res, find where key (count) appears & append value s (the word) to end of list

    return res.values()
    

strs = ["eat","tea","tan","ate","nat","bat"]
result = groupAnagrams(strs)
print("\n")
print(result) 
print("\n")