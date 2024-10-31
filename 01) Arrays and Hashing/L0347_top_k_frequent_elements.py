
# nums = [1,1,1,1,  6,6,  9]    k= 2
def topKFrequent_neetCode(nums: list[int], k):

    # countDict=  {1: 4,          6: 2,           9: 1}
    #             {1_val:4count,  6_val: 2count,  9_val:1count}
    countDict = {}
    for number in nums:
        countDict[number] = 1 + countDict.get(number, 0)

    # freq= [[],   [],   [],  [],   [],   [],   [],   []]
    #      0:[]  1:[]  2:[]  3[]  4:[]  5:[]  6:[],  7[]
    freq = [[] for i in range(len(nums) + 1)]

    # freq= [[],        [9],             [6],      [],         [1],       [],   [],  []]
    #      0:[]  1count:[9_val]  2count: [6_val]  3[]]  count4:[1_val]  5:[]  6:[]  7[]
    for number, count in countDict.items():
        freq[count].append(number)

   # loop backward through freq
    res = []
    for i in range(len(freq)-1, -1, -1):
        for number in freq[i]:
            res.append(number)

            if len(res) == k:
                return res


def topKFrequent_solution(nums: list[int], k):
    countDict = {}
    for i in nums:
        countDict[i] = 1 + countDict.get(i, 0)
    sortedDict = dict(
        sorted(countDict.items(), key=lambda x: x[1], reverse=True))
    return list(sortedDict.keys())[:k]


def topKFrequent(nums: list[int], k):
    counter = {}

    for num in nums:
        counter[num] = 1 + counter.get(num, 0)

    res = []
    for i in range(k):
        curr_max = max(counter, key=counter.get) # find key in counter with highest value.
        res.append(curr_max)
        counter.pop(curr_max) # pop highest max # from counter and restart

    return res


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


# def topKFrequent(nums: list[int], k):
#     ##########################################################################
#     # (1) Creating "Count" dictionary & storing number of times number occurs
#     ##########################################################################
#     # empty dictionary
#     count = {}

#     # counting the number of times each value in nums occurs and store in count
#     for number in nums:
#         count[number] = 1 + count.get(number, 0) # [1: 3 times]
#                                                  # [2: 2 times]
#                                                  # [3: 1 time]

#     ###########################################################################################
#     # (2) Creating "frequency" array w/ index representing number & value representing count
#     ###########################################################################################
#     # initializing array with empty spots equal to size of input array. length of 6 --> 6 spots
#     # 0: []  1: []  2: []  3:[]  4:[]  5:[]  6:[]
#     freq = [ [] for i in range(len(nums) + 1) ] # initialize as empty array
#                                                 # the num of empty arrays that go in there...
#                                                 # is size of input + 1 (if not, will go up to 5)


#     # NOTE: Count uses key-value pair as [number : count]
#     # looking at both of these values, append to frequency the appropriate values
#     # at index of count in frequency, append number
#     # ...
#     # example: index 1 represents number 1...
#     # value of index represents count of number...
#     # which will update (0 --> 1 ---> 2 ---> 3) as 1 is counted how many times it appears
#     for number, count in count.items():
#         freq[count].append(number) # in frequency array, at index count, append to list value number

#     ###############################################################################
#     # (3) Creating "result" array & calculating most frequent k values to display
#     ###############################################################################
#     res = []

#     # range(starting_index, last_index, increment)
#     # go from lenth(freq) - 1
#     for i in range(len(freq) - 1, -1, -1):
#         for n in freq[i]:
#             res.append(n)

#             if len(res) == k:
#                 return res
