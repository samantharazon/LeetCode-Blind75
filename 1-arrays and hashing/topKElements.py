
# [1, 1, 1, 2, 2, 3, 4, 4, 4]
#
# three 1's, two 2's, one 3, three 4's
#
# i(count)  0   1   2      3     4   5   6   (6 is length of array)
# values       [3] [2]  [1, 4]
#
# go from left to right
#

def topKFrequent(nums: list[int], k):
    #####################################################################
    # (1) Creating "Count" dictionary & storing number of times number occurs
    # {1: 3 times,      2: 2 times,     3: 1 time}
    countDict = {}

    for number in nums:
        countDict[number] = 1 + countDict.get(number, 0)
    
    #####################################################################
    # (2) Creating "frequency" array  << Index=Number Value=Count >>
    # w/ index representing number & value representing count
    # 0: []  1: []  2: []  3:[]  4:[]  5:[]  6:[] 
    freq = [ [] for i in range(len(nums) + 1) ]

    # NOTE: countDict uses key-value pair as [number : count]
    # in frequency, using the VALUE:count as the index, append to list the KEY:number
    # 0: []  1: [3]  2: [2]  3:[1]  4:[]  5:[]  6:[] 
    for number, count in countDict.items():
        freq[count].append(number)

    #####################################################################
    # (3) Creating "result" array & calculating most frequent k values to display
    res = []

    # NOTE: range(starting_index, last_index, increment)
    # traverse below array from end to beginning and append to res
    # when length of res equals k, stop
    # 0: []  1: [3]  2: [2]  3:[1]  4:[]  5:[]  6:[] 
    for i in range(len(freq)-1, -1, -1):

        for number in freq[i]:
            res.append(number)

            if len(res) == k:
                return res


nums = [1,1,1, 2,2, 3]
k = 2
result = topKFrequent(nums, k)
print("\nResult: ", result)

nums = [1]
k = 1
result = topKFrequent(nums, k)
print("\nResult: ", result)

nums = [1,1,  2,2,2,2,  3,  4,4,  5,5,5,  6,6,6,6,6,6]
k = 3
result = topKFrequent(nums, k)
print("\nResult: ", result)


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
