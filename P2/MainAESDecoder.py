import sys
from AESDecoder import AES128Decoder
from BlockMode import *
from Utils import *

cypher_file = open("./2017_09_26_13_22_54_mario.fernandez.enc",'r',encoding="ISO-8859-1")
key_file = open("./2017_09_26_13_22_54_mario.fernandez.key",'r',encoding="ISO-8859-1")

text = cypher_file.read()
key = key_file.read()

blocks = ECB128(text, "ISO-8859-1")
keyBlock = ECB192(key, "ISO-8859-1")[0]
printBlockHex(keyBlock)
M = ""

for i in range(len(blocks)):
    Maux = AES128Decoder(blocks[i], keyBlock)
    M = M + InvECB(Maux)
    
print(M)
