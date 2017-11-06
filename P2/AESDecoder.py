from GFFunctions import *
from Utils import *

Nr = 12
Nk = 192/32
Nb = 4

def initializeRcon():
    global Nr
    Rcon = [[0 for x in range(4)] for y in range(10)]
    Rcon[0][0] = 1
    for j in range(1,10):
        Rcon[j][0] = GF_product_t(2, Rcon[j-1][0])
    return Rcon

Rcon = initializeRcon()

def RotByte(word):
    firstByte = word[0]
    for i in range(3):
        word [i] = word [i+1]
    word[3] = firstByte

def InvRotByte(word):
    lastByte = word[3]
    for i in range(1,4):
        word [i] = word [(i+1)%4]
    word[0] = lastByte

 
def InvByteSubWord(word):
    for i in range(len(word)):
        byte = GF_invers(word[i])
        bits = byte2bits(byte)
        negOnes = [-1,-1,0,0,0,-1,-1,0]
        bits = addLists([bits,negOnes])
        l0 = [bits[7]*x for x in [0,1,0,1,0,0,1,0]]
        l1 = [bits[6]*x for x in [0,0,1,0,1,0,0,1]]
        l2 = [bits[5]*x for x in [1,0,0,1,0,1,0,0]]
        l3 = [bits[4]*x for x in [0,1,0,0,1,0,1,0]]
        l4 = [bits[3]*x for x in [0,0,1,0,0,1,0,1]]
        l5 = [bits[2]*x for x in [1,0,0,1,0,0,1,0]]
        l6 = [bits[1]*x for x in [0,1,0,0,1,0,0,1]]
        l7 = [bits[0]*x for x in [1,0,1,0,0,1,0,0]]
        newBits = list(addLists([l0,l1,l2,l3,l4,l5,l6,l7]))
        newBits.reverse()
        word[i] = bits2byte(newBits)
 
def InvByteSub(block):
    for i in range(len(block)):
        InvByteSubWord(block[i])
        
def ByteSubWord(word):
    for i in range(len(word)):
        byte = GF_invers(word[i])
        bits = byte2bits(byte)
        l0 = [bits[7]*x for x in [1,1,1,1,1,0,0,0]]
        l1 = [bits[6]*x for x in [0,1,1,1,1,1,0,0]]
        l2 = [bits[5]*x for x in [0,0,1,1,1,1,1,0]]
        l3 = [bits[4]*x for x in [0,0,0,1,1,1,1,1]]
        l4 = [bits[3]*x for x in [1,0,0,0,1,1,1,1]]
        l5 = [bits[2]*x for x in [1,1,0,0,0,1,1,1]]
        l6 = [bits[1]*x for x in [1,1,1,0,0,0,1,1]]
        l7 = [bits[0]*x for x in [1,1,1,1,0,0,0,1]]
        ones = [1,1,0,0,0,1,1,0]
        newBits = list(addLists([l0,l1,l2,l3,l4,l5,l6,l7,ones]))
        newBits.reverse()
        word[i] = bits2byte(newBits)
 
def ByteSub(block):
    for i in range(len(block)):
        ByteSubWord(block[i])
 
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
        RotByte(lastWord)
        ByteSubWord(lastWord)
        W[4*i] = addLists([W[4*(i-1)], lastWord, Rcon[i-1]])
        lastWord = W[4*i]
        for j in range(1,4):
            W[4*i + j] = addLists([lastWord, W[4*(i-1) + j]])
            lastWord = W[4*i + j]
    return W


def InvShiftRow(block):
    # Transpose the block for esasier manipulation
    transposedBlock = list(map(list, zip(*block)))
    for i in range (len(block)):
        for j in range(i):
            InvRotByte(transposedBlock[i])
    
    # Detranspose the block. Note: It can't be done in the same way that before cause this is a reasignation of a reference
    for i in range(len(block)):
        for j in range(len(block[i])):
            block[i][j] = transposedBlock[j][i] 
    
def InvMixColumn(block):
    for i in range(len(block)):
        word = list(block[i])
        l0 = [GF_product_t(block[i][0],x) for x in [0x0E,0x09,0x0D,0x0B]]
        l1 = [GF_product_t(block[i][1],x) for x in [0x0B,0x0E,0x09,0x0D]]
        l2 = [GF_product_t(block[i][2],x) for x in [0x0D,0x0B,0x0E,0x09]]
        l3 = [GF_product_t(block[i][3],x) for x in [0x09,0x0D,0x0B,0x0E]]
        block[i] = addLists([l0,l1,l2,l3])
    
def AddRoundKey(state, roundKey):
    for i in range(len(state)):
        state[i] = addLists([state[i], roundKey[i]])    
    
def AES128Decoder(block, key):
    global Nr
    state = list(block)
    roundKeys = KeyExpansion(key)
    AddRoundKey(state, roundKeys[0:4])
    for i in range(1, Nr):
        InvByteSub(state)
        InvShiftRow(state)
        InvMixColumn(state)
        invRoundKey_i = InvMixColumn(list(roundKeys[4*i:4*(i+1)]))
        AddRoundKey(state, invRoundKey_i)
    InvByteSub(state)
    InvShiftRow(state)
    AddRoundKey(state, roundKeys[4*Nr:4*(Nr+1)])
    return state
