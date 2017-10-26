def byte2bits(byte):
    bits = []

    bits.append(0 if byte%2 == 0 else 1)
    while byte > 1:
        byte = byte // 2
        bits.append(0 if byte%2 == 0 else 1)
    for i in range(len(bits),8):
        bits.append(0)
    bits.reverse()
    if len(bits) > 8:
        sys.exit("ERROR en el nombre {}, excedeix 8 bits".format(byte))
    return bits

def bits2byte(bits):
    byte = 0
    for i in range(8):
        byte += bits[i]*pow(2,7-i)
    return byte
 
def bitWiseXor(a,b):
    return a^b
 
def addLists(llistes):
    result = map(bitWiseXor,llistes[0],llistes[1])
    for i in range(2, len(llistes)):
        result = map(bitWiseXor,result,llistes[i])
    return list(result)

def addBlocks(blockA, blockB):
    result = list(blockA)
    for i in range(len(blockA)):
        result[i] = addLists([result[i], blockB[i]])
    return result
    
def printBlockHex(block):
    for i in range(len(block)):
        print("")
        for j in range(len(block[i])):
            print("{} ".format(hex(block[i][j])), end='')
 
