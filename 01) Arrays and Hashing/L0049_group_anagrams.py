from collections import defaultdict

def groupAnagrams(str_array):
    # goal:   {aet: [eat, tea, ate],  ant: [tan, nat]}
    anagram_map = defaultdict(list)  # defaultdict never raises a KeyError.
    for word in str_array:
        # '' is separator between each letter
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word].append(word)
    print("dict:", dict(anagram_map))
    return list(anagram_map.values())


''' ALT SOLUTION: NEETCODE
def groupAnagrams_NEETCODE(strs: list[str]):
    # goal:   {0 1 0 1 ... 0 0: [eat, tea, ate]}
    # means:  {a thru z letters :  matching words }
    # defaultdict auto assigns default value to non-existent key
    res = defaultdict(list)

    for word in strs:
        # [0 1 0 1 ...]    0 = does not appear, 1 = appear once, 2 = appear twice..
        count = [0] * 26

        for letter in word:
            # map 'a' to index 0...   map 'z' to index 25.
            count[ord(letter) - ord("a")] += 1

        # find where count appears & append word
        res[tuple(count)].append(word)
    return res.values()
    
    # res = {
    # (1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['eat', 'tea', 'ate'], 
    # (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['tan', 'nat'], 
    # (1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['bat']})
    
'''

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print("\nstrs:", strs)
result = groupAnagrams(strs)
print("result=", result)

print("\n")
