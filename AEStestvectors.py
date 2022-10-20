import random

def hex_number( count, padded=False ):
    # This currently generates a number of length count hex digits.
    # Pad on the left with 0's if padded is True:
    x = random.randint( 0, 16**count )
    hexdig = "%x" % x
    if padded:
        out = hexdig.zfill( count ) # pad with 0 if necessary
        return out
    else:
        return hexdig

def AESvectors(size, num, padded):
    # generate num vectors (one per line) of size at most count
    # hex digits
    lst = []
    for i in range(num):
        lst.append(hex_number(size, padded))
    return lst

# Set the last param to True to pad all lines size hex digits.
# The padding is only needed for lines that have leading 0's.
lst = AESvectors(size=32, num=1, padded=False)
file = open("input.pt", "w")
for vector in lst:
    if (lst[-1] == vector):
        file.write(vector)
    else:
        file.write(vector+"\n")