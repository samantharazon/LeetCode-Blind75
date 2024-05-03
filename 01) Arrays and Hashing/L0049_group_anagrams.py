from collections import defaultdict

def groupAnagrams (strs: list[str]):
    
    # goal:   {0 1 0 1 ... 0 0: eat, tea, ate} 
    # means:  {a thru z letters :  matching words }

    # defaultdict auto assigns default value to non-existent key
    res = defaultdict(list)
    
    for word in strs:
        # count = 0(letterA), 0(letterB), 0(letterC)...
        # 0 = does not appear, 1 = appear once, 2 = appear twice..
        count = [0] * 26 

        for letter in word: 
             # map 'a' to index 0... map 'z' to index 25.
            count[ord(letter) - ord("a")] += 1 
                                             
        # find where count appears & append word
        # [count, words]  ---> {0 1 0 1 ... 0 0, eat, tea, ate} 
        res[tuple (count)].append(word) 

    return res.values()
    

strs = ["eat","tea","tan","ate","nat","bat"]
result = groupAnagrams(strs)
print("\n")
print(result) 
print("\n")
