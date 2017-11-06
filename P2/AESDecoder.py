from GFFunctions import *
from Utils import *
import sys

Nr = 12
Nk = 0
Nb = 0

def initializeRcon():
    Rcon = [[0 for x in range(4)] for y in range(Nr)]
    Rcon[0][0] = 1
    for j in range(1,Nr):
        Rcon[j][0] = GF_product_t(2, Rcon[j-1][0])
    return Rcon

def RotByte(word):
    firstByte = word[0]
    for i in range(3):
        word [i] = word [i+1]
    word[3] = firstByte

def InvRotByte(word):
    lastByte = word[3]
    for i in range(1,4):
        j = 4-i
        word [j] = word [j-1]
    word[0] = lastByte

 
def InvByteSubWord(word):
    ones = [1,1,0,0,0,1,1,0]
    ones.reverse()
    for i in range(len(word)):
        bits = byte2bits(word[i])
        bits = list(addLists([bits,ones]))
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
        word[i] = GF_invers(bits2byte(newBits))

 
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
    global Nr, Nk, Nb
    Rcon = initializeRcon()
    W = [[0 for x in range(len(key[0]))] for y in range(len(key)*(Nr +1))]
    # Initial copy of the cypher key
    for i in range(Nk):
        for j in range(4):
            W[i][j] = key[i][j]
    
    # Main loop
    for i in range(1, Nr+1):
        lastWord = list(W[Nk-1 + Nk*(i-1)])
        RotByte(lastWord)
        ByteSubWord(lastWord)
        W[Nk*i] = addLists([W[Nk*(i-1)], lastWord, Rcon[i-1]])
        lastWord = W[Nk*i]
        for j in range(1,Nk):
            W[Nk*i + j] = addLists([lastWord, W[Nk*(i-1) + j]])
            lastWord = W[Nk*i + j]
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
    global Nk, Nb, Nr
    Nb = len(block) * len(block[0]) * 8 // 32
    Nk = len(key) * len(key[0]) * 8 // 32
    if Nk == 8 or Nb == 8:
        Nr = 14
    elif Nk == 6 or Nb == 6:
        Nr = 12
    else:
        Nr = 10
    state = list(block)
    roundKeys = KeyExpansion(key)
    AddRoundKey(state, roundKeys[4*Nr:4*(Nr+1)])
    for i in range(1, Nr):
        j = Nr - i
        InvByteSub(state)
        InvShiftRow(state)
        InvMixColumn(state)
        invRoundKey_i = list(roundKeys[4*j:4*(j+1)])
        InvMixColumn(invRoundKey_i)
        AddRoundKey(state, invRoundKey_i)
    InvByteSub(state)
    InvShiftRow(state)
    AddRoundKey(state,  roundKeys[0:4])
    return state
