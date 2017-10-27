import sys
from random import randint
from AES import AES128
from AESByteSubIdentity import AES128 as AES128ByteSubIdentity
from BlockMode import *
from Utils import *

# True if exclusiveOr(sumTerms) = target, False otherwise
def checkSum(target, sumTerms):
        pass


with open('./out/CheckAESByteSubIdentityCypher.txt','w') as f:
    f.write("CheckAESCypher(AES, C, i, j) = 1 -> Given a AES implementation ('ByteSubIdentity', 'regular'), a cypher text and 2 integers i j; C == C_i + C_j + C_ij (+ means exclusive or)\n")
    f.write("CheckAESCypher(AES, C, i, j) = 1 -> Given a AES implementation ('ByteSubIdentity', 'regular'), a cypher text and 2 integers i j; C != C_i + C_j + C_ij (+ means exclusive or)\n\n\n")
    f.write("{:<40}{:<40}{:<8}{:<8}{:<40}{:<40}\n".format("text","key",'i','j',"CheckAESCypher('regular', C, i, j)", "CheckAESCypher('ByteSubIdentity', C, i, j)"))
    for i in range(32):
        for j in range(32):
            key = generateRandomText()
            keyBlock = ECB(key)[0]
            text = generateRandomText(32)
            blocks = ECB(text)
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
