import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from random import randint
from AES import AES128
from AESByteSubIdentity import AES128 as AES128ByteSubIdentity
from AESShiftRowIdentity import AES128 as AES128ShiftRowIdentity
from AESMixColumnIdentity import AES128 as AES128MixColumnIdentity
from BlockMode import *
from Utils import *
import sys


# 2.1 Efectes de les funcions elementals

# 2.1.1  

with open('./out/CheckAESByteSubIdentityCypher.txt','w') as f:
    f.write("CheckAESCypher(AES, C, i, j) = 1 -> Given a AES implementation ('ByteSubIdentity', 'regular'), a cypher text and 2 integers i j; C == C_i + C_j + C_ij (+ means exclusive or)\n")
    f.write("CheckAESCypher(AES, C, i, j) = 0 -> Given a AES implementation ('ByteSubIdentity', 'regular'), a cypher text and 2 integers i j; C != C_i + C_j + C_ij (+ means exclusive or)\n\n\n")
    f.write("{:<40}{:<40}{:<8}{:<8}{:<40}{:<40}\n".format("text","key",'i','j',"CheckAESCypher('regular', C, i, j)", "CheckAESCypher('ByteSubIdentity', C, i, j)"))
    for experiment in range(1000):
        i = randint(0, 127)
        j = randint(0, 127)
        key = generateRandomText()
        keyBlock = ECB128(key,"utf-8")[0]
        text = generateRandomText(32)
        blocks = ECB128(text,"utf-8")
        checkRegular = 0
        checkIdentity = 1
        for k in range(len(blocks)):
            block = blocks[k]
            block_i = changeBitBlock(block, i)
            block_j = changeBitBlock(block, j)
            block_ij = changeBitBlock(block_i, j)
            
            C = AES128(block, keyBlock)
            C_i = AES128(block_i, keyBlock)
            C_j = AES128(block_j, keyBlock)
            C_ij = AES128(block_ij, keyBlock)
            
            if checkSum(C,[C_i, C_j, C_ij]):
                checkRegular = 1                                        
            
            C = AES128ByteSubIdentity(block, keyBlock)
            C_i = AES128ByteSubIdentity(block_i, keyBlock)
            C_j = AES128ByteSubIdentity(block_j, keyBlock)
            C_ij = AES128ByteSubIdentity(block_ij, keyBlock)
            
            if not checkSum(C,[C_i, C_j, C_ij]):
                checkIdentity = 0
                
        f.write("{:<40}{:<40}{:<8}{:<8}{:<40}{:<40}\n".format(text,key,i,j, checkRegular, checkIdentity))

f.closed

# 2.1.2  

with open('./out/CheckAESShiftRowIdentityCypher.txt','w') as f:
    for k in range(10):
        i = randint(0, 127)
        key = generateRandomText()
        keyBlock = ECB128(key,"utf-8")[0]
        text = generateRandomText()
        blocks = ECB128(text,"utf-8")
        block = blocks[0]
        C = AES128ShiftRowIdentity(block, keyBlock)
        block_i = changeBitBlock(block,i)
        C_i = AES128ShiftRowIdentity(block_i, keyBlock)
          
        if i != 0:
            f.write("\n------------------------------------\n")
        f.write("text = {}\n".format(text))
        f.write("key = {}\n".format(key))
        f.write("i = {}\n".format(i))
        f.write("M = \n")
        printInFileBlockHex(blocks[0], f)
        f.write("\n\nM_i = \n")
        printInFileBlockHex(block_i, f)
        f.write("\n\nC = \n")
        printInFileBlockHex(C, f)
        f.write("\n\nC_i = \n")
        printInFileBlockHex(C_i, f)

f.closed

# 2.1.3  

with open('./out/CheckAESMixColumnIdentityCypher.txt','w') as f:
     for k in range(10):
        i = randint(0, 127)
        key = generateRandomText()
        keyBlock = ECB128(key,"utf-8")[0]
        text = generateRandomText()
        blocks = ECB128(text,"utf-8")
        block = blocks[0]
        C = AES128MixColumnIdentity(block, keyBlock)
        block_i = changeBitBlock(block,i)
        C_i = AES128MixColumnIdentity(block_i, keyBlock)
          
        if i != 0:
            f.write("\n------------------------------------\n")
        f.write("text = {}\n".format(text))
        f.write("key = {}\n".format(key))
        f.write("i = {}\n".format(i))
        f.write("M = \n")
        printInFileBlockHex(blocks[0], f)
        f.write("\n\nM_i = \n")
        printInFileBlockHex(block_i, f)
        f.write("\n\nC = \n")
        printInFileBlockHex(C, f)
        f.write("\n\nC_i = \n")
        printInFileBlockHex(C_i, f)

f.closed

# 2.2  Propagació de petits canvis

key = generateRandomText()
keyBlock = ECB128(key,"utf-8")[0]
text = generateRandomText()
blocks = ECB128(text,"utf-8")
block = blocks[0]
C = AES128(block, keyBlock)

x_axis = [x for x in range(128)]
y_axis_bits_message = [0 for _ in range(128)]
y_axis_pos_message = [0 for _ in range(128)]
y_axis_bits_key = [0 for _ in range(128)]
y_axis_pos_key = [0 for _ in range(128)]

for i in range(128):
    block_i = changeBitBlock(block,i)
    C_i = AES128(block_i, keyBlock)
    [numberOfDifferentBits, positions] = compareBlocks(C, C_i)
    
    y_axis_bits_message[numberOfDifferentBits] = y_axis_bits_message[numberOfDifferentBits] + 1
    for bit in positions:
        y_axis_pos_message[bit] = y_axis_pos_message[bit] + 1
    
    keyBlock_i = changeBitBlock(keyBlock,i)
    C_i = AES128(block, keyBlock_i)
    [numberOfDifferentBits, positions] = compareBlocks(C, C_i)

    y_axis_bits_key[numberOfDifferentBits] = y_axis_bits_key[numberOfDifferentBits] + 1
    for bit in positions:
        y_axis_pos_key[bit] = y_axis_pos_key[bit] + 1

# Histogram of # changed bits changing a bit in message
fig, ax = plt.subplots()
ax.bar(x_axis, y_axis_bits_message, width = 0.8, align="center")
plt.xlabel('# changed bits')
plt.ylabel('# apperances')
plt.show()
plt.savefig('./out/hist1.png', bbox_inches='tight')
plt.close(fig)

# Histogram of # positions changed changing bit in message
fig, ax = plt.subplots()
ax.bar(x_axis, y_axis_pos_message, width = 0.8, align="center")
plt.xlabel('Bit position')
plt.ylabel('# apperances')
plt.show()
plt.savefig('./out/hist2.png', bbox_inches='tight')
plt.close(fig)

# Histogram of # changed bits changing a bit in key
fig, ax = plt.subplots()
ax.bar(x_axis, y_axis_bits_key, width = 0.8, align="center")
plt.xlabel('# changed bits')
plt.ylabel('# apperances')
plt.show()
plt.savefig('./out/hist3.png', bbox_inches='tight')
plt.close(fig)

# Histogram of # positions changed changing bit in key
fig, ax = plt.subplots()
ax.bar(x_axis, y_axis_pos_key, width = 0.8, align="center")
plt.xlabel('Bit position')
plt.ylabel('# apperances')
plt.show()
plt.savefig('./out/hist4.png', bbox_inches='tight')
plt.close(fig)
