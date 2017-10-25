from GFFunctions import *
from operator import add

Nr = 10;
Nk = 128/32;
Nb = 4;

def initializeRcon():
    global Nr
    Rcon = [[0 for x in range(4)] for y in range(10)]
    Rcon[0][0] = 1
    for j in range(1,10):
        Rcon[j][0] = GF_product_t(2, Rcon[j-1][0])
    return Rcon

Rcon = initializeRcon()

def rotByte(word):
    firstByte = word[0]
    for i in range(3):
        word [i] = word [i+1]
    word[3] = firstByte
 
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
 
def sumaLlistes(llistes):
    result = map(bitWiseXor,llistes[0],llistes[1])
    for i in range(2, len(llistes)):
        result = map(bitWiseXor,result,llistes[i])
    return list(result)

def byteSubAux(bits):
    l0 = [bits[7]*x for x in [1,1,1,1,1,0,0,0]]
    l1 = [bits[6]*x for x in [0,1,1,1,1,1,0,0]]
    l2 = [bits[5]*x for x in [0,0,1,1,1,1,1,0]]
    l3 = [bits[4]*x for x in [0,0,0,1,1,1,1,1]]
    l4 = [bits[3]*x for x in [1,0,0,0,1,1,1,1]]
    l5 = [bits[2]*x for x in [1,1,0,0,0,1,1,1]]
    l6 = [bits[1]*x for x in [1,1,1,0,0,0,1,1]]
    l7 = [bits[0]*x for x in [1,1,1,1,0,0,0,1]]
    uns = [1,1,0,0,0,1,1,0]
    mapl = sumaLlistes([l0,l1,l2,l3,l4,l5,l6,l7,uns])
    newBits = list(mapl)
    newBits.reverse()
    return newBits
 
def byteSub(word):
    for i in range(len(word)):
        byte = GF_invers(word[i])
        bits = byte2bits(byte)
        word[i] = bits2byte(byteSubAux(bits))
    return word
 
def KeyExpansion(key):
    global Nr, Nk, Nb, Rcon
    W = [[0 for x in range(4)] for y in range(4*(Nr +1))]
    
    # Initial copy of the cypher key
    for i in range(4):
        for j in range(4):
            W[i][j] = key[i][j]
    
    # Main loop
    for i in range(1, Nr+1):
        lastWord = list(W[3 + 4*(i-1)])
        rotByte(lastWord)
        byteSub(lastWord)
        W[4*i] = sumaLlistes([W[4*(i-1)], lastWord, Rcon[i-1]])
        lastWord = W[4*i]
        for j in range(1,4):
            W[4*i + j] = sumaLlistes([lastWord, W[4*(i-1) + j]])
            lastWord = W[4*i + j]
    return W

KeyExpansion([[0x2b,0x7e,0x15,0x16],[0x28,0xae,0xd2,0xa6],[0xab,0xf7,0x15,0x88],[0x09,0xcf,0x4f,0x3c]])

#def AES128(block, key):
    #global Nr
    #state = block
    #roundKeys = ExpandKey(key)
    #AddRoundKey(state, roundKeys[0])
    #for i in range(1:Nr-1):
        #ByteSub(state)
        #ShiftRow(state)
        #MixColumn(state)
        #AddRoundKey(state, roundKeys[i])
    #ByteSub(state)
    #ShiftRow(state)
    #AddRoundKey(state, roundKeys[Nr])
    #return state
