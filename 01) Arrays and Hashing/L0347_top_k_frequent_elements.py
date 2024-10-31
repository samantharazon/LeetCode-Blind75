

def topKFrequent(nums: list[int], k):
    counter = {}

    for num in nums:
        counter[num] = 1 + counter.get(num, 0)

    res = []
    for i in range(k):
        # find key in counter with highest value.
        curr_max = max(counter, key=counter.get)
        res.append(curr_max)
        counter.pop(curr_max)  # pop highest max # from counter and restart

    return res

''' SORTDICT
def topKFrequent_sortDict(nums: list[int], k):
    countDict = {}
    for i in nums:
        countDict[i] = 1 + countDict.get(i, 0)
    sortedDict = dict(
        sorted(countDict.items(), key=lambda x: x[1], reverse=True))
    return list(sortedDict.keys())[:k]
'''

''' NEETCODE
# nums = [1,1,1,1,  6,6,  9]    
# k= 2
def topKFrequent_NEETCODE(nums: list[int], k):

    # countDict= {1_val:4times,  6_val: 2times,  9_val:1times}
    countDict = {}
    for number in nums:
        countDict[number] = 1 + countDict.get(number, 0) 

    # freq= [[],   [],   [],   [],   [],   [],   [],   []]
    # index:  0     1     2     3     4     5    6     7
    # index represents number. value it has represents times it appears
    freq = [[] for i in range(len(nums) + 1)]

    # freq= [[],   [9],       [6],      [],     [1],   [],   [],   []]
    # index:  0     1          2        3        4     5     6     7
    #           9 appears   6 appears          1 appears
    #            1 time      2 times            4 times
    for number, count in countDict.items():
        freq[count].append(number)

   # loop backward through 
    # range(starting_index, last_index, increment)
    # go from lenth(freq) - 1
    res = []
    for i in range(len(freq)-1, -1, -1):
        for number in freq[i]:
            res.append(number)

            if len(res) == k:
                return res
'''

nums = [99, 100, 100, 100, 100,  88,  600, 600, 600]
k = 2
print("\nnums: ", nums)
print("k= ", k)
result = topKFrequent(nums, k)
print("Result: ", result)  # [1, 6]

nums = [1]
k = 1
print("\nnums: ", nums)
print("k= ", k)
result = topKFrequent(nums, k)
print("Result: ", result)  # [1]

nums = [1, 1,  2, 2, 2, 2,  3,  4, 4,  5, 5, 5,  6, 6, 6, 6, 6, 6]
k = 3
print("\nnums: ", nums)
print("k= ", k)
result = topKFrequent(nums, k)
print("Result: ", result)  # [6, 2, 5]
