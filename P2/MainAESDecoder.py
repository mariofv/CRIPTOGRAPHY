import os
from AESDecoder import AES128Decoder
from AES import AES128
from BlockMode import *
from Utils import *

cypher_file = open("./in/2017_09_26_13_22_54_mario.fernandez.enc",'r',encoding="ISO-8859-1")
key_file = open("./in/2017_09_26_13_22_54_mario.fernandez.key",'r',encoding="ISO-8859-1")

text = cypher_file.read()
key = key_file.read()

blocks = ECB128(text, "ISO-8859-1")
keyBlock = ECB192(key, "ISO-8859-1")[0]


M = ""

l = len(blocks)
for i in range(l):
    if i%100 == 0:
        os.system('clear') 
        print("{}%".format(i/l))
    Maux = AES128Decoder(blocks[i], keyBlock)
    M = M + block2String(Maux,"ISO-8859-1")
    
    with open('./out/2017_09_26_13_22_54_mario_fernandez.jpg','w') as f:
    f.write(M)
f.closed

