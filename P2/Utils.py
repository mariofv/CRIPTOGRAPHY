import string
import random
import copy
from random import randint

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
 
def block2String(block):
    text = ""
    for i in range(len(block)):
        for j in range(len(block[i])):
            text = text + (bytes.fromhex(hex(block[i][j])).decode('utf-8'))
 
def bitWiseXor(a,b):
    return a^b
 
def addLists(llistes):
    result = map(bitWiseXor,llistes[0],llistes[1])
    for i in range(2, len(llistes)):
        result = map(bitWiseXor,result,llistes[i])
    return list(result)

def addBlocks(blocks):
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
            
def printInFileBlockHex(block,f):
    for i in range(len(block)):
        f.write("\n")
        for j in range(len(block[i])):
            if j != 0:
                f.write(" ")
            f.write("{}".format(hex(block[i][j])))

def printBlockBit(block):
    for i in range(len(block)):
        print("")
        for j in range(len(block[i])):
            print("{0:08b} ".format(block[i][j]), end='')
            
def printInFileBlockBit(block,f):
    for i in range(len(block)):
        f.write("\n")
        for j in range(len(block[i])):
            if j != 0:
                f.write(" ")
            f.write("{0:08b}".format(block[i][j]))

def generateRandomText(maxLength = -1):
    chars = string.ascii_letters + string.digits
    if maxLength <= 0:
        length = 32 
    else:
        length = randint(1, maxLength)
    return ''.join(random.choice(chars) for _ in range(length))

def negateBit(bit):
    return 0 if bit == 1 else 1

def changeBitBlock(block, bit):    
    newBlock = copy.deepcopy(block)
    byte2select = bit//8
    bit2select = bit%8
    selectedByte = newBlock[byte2select//4][byte2select%4]
    bits = byte2bits(selectedByte)
    bits[bit2select] = negateBit(bits[bit2select])
    newBlock[byte2select//4][byte2select%4] = bits2byte(bits)
    
    return newBlock

# True if exclusiveOr(sumTerms) = target, False otherwise
def checkSum(target, sumTerms):
    n = len(target) 
    m = len(target[0])
    for i in range(n):
        for j in range(m):
            result = 0
            for k in range(len(sumTerms)):
                result = bitWiseXor(sumTerms[k][i][j], result)
            if result != target[i][j]:
                return False
    return True

## Returns a pair [a,b] where a is the # of different bits and b is the positions of that different bits between blocks X and Y
def compareBlocks(X,Y):
    differentBits = 0
    positions = []
    for i in range(len(X)):
        for j in range(len(X[i])):
            bitsX = byte2bits(X[i][j])
            bitsY = byte2bits(Y[i][j])
            for k in range(len(bitsX)):
                if bitsX[k] != bitsY[k]:
                    differentBits = differentBits + 1
                    positions.append(i*32 + j*8 + k)
                    
    return [differentBits, positions]
