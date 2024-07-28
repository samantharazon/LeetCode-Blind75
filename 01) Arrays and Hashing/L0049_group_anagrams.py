from collections import defaultdict

def groupAnagrams_2 (strs: list[str]):
    # goal:   {0 1 0 1 ... 0 0: [eat, tea, ate]} 
    # means:  {a thru z letters :  matching words }

    res = defaultdict(list) # defaultdict auto assigns default value to non-existent key
    
    for word in strs:
        count = [0] * 26 # [0 1 0 1 ...]    0 = does not appear, 1 = appear once, 2 = appear twice..

        for letter in word: 
            count[ord(letter) - ord("a")] += 1 # map 'a' to index 0... map 'z' to index 25.
                                             
        res[tuple (count)].append(word)  # find where count appears & append word   [count, words]  ---> {0 1 0 1 ... 0 0, eat, tea, ate} 

    return res.values()
    

def groupAnagrams(str_array):
    # goal:   {aet: [eat, tea, ate],  ant: [tan, nat]}
    anagram_map = defaultdict(list) # defaultdict never raises a KeyError. 
    for word in str_array:
       sorted_word = ''.join(sorted(word)) # '' is separator between each letter 
       anagram_map[sorted_word].append(word)
    # print(dict(anagram_map))
    
    return list(anagram_map.values())


strs = ["eat","tea","tan","ate","nat","bat"]
result = groupAnagrams(strs)
print("\n")
print(result) 
print("\n")
