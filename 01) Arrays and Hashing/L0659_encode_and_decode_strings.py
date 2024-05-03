
def encode(input):
    res = ""
    for word in input:
        res += str(len(word)) + "#" + word 
    return res

def decode(input):
    res, curr_pos = [], 0 

    while curr_pos < len(input):  
        pound_pos = curr_pos       

        while input[pound_pos] != "#":
            pound_pos += 1          

        length = int(input[curr_pos:pound_pos]) 
        res.append(input[pound_pos+1 : pound_pos+1+length]) 
        curr_pos = pound_pos + 1 + length 
        
    return res


input = ["lint", "code", "love", "you"]
encoded = encode(input)
print("\nEncoded: ", encoded)
decoded = decode(encoded)
print("Decoded: ", decoded)
print()

input = ["we", "say", ":", "yes"]
encoded = encode(input)
print("\nEncoded: ", encoded)
decoded = decode(encoded)
print("Decoded: ", decoded)
print()

input = ["neet", "code"]
encoded = encode(input)
print("\nEncoded: ", encoded)
decoded = decode(encoded)
print("Decoded: ", decoded)
print()
