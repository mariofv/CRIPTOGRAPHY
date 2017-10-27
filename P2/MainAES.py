from AES import *
from BlockMode import *
from Utils import *

key = generateRandomKey()
text = generateRandomText(32)

blocks = ECB(text)
keyBlock = ECB(key)[0]

for i in range(len(blocks)):
    cypherBlock = AES128(blocks[i], keyBlock)
