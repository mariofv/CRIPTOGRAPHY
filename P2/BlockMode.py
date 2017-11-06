import binascii

# Adds PKCS5 Padding to a given hex string
def PKCS5Padding(hexByteText):
    textLength = len(hexByteText)//2
    paddingBytes = (32 - textLength%32)%32
    paddedText = hexByteText
    for i in range(paddingBytes):
        paddedText = paddedText + binascii.hexlify(bytes([paddingBytes]))
    return paddedText

# Transform text in len(textInHex)/32 blocks of 128 bits each (PKCS5 padding). 
def ECB128(text, encodingType):
    byteText = bytes(text, encoding=encodingType)
    hexByteText = binascii.hexlify(byteText)
    paddedText = PKCS5Padding(hexByteText)
    blocks = []
    for i in range(len(paddedText)//32):
        actualBlock = []
        subString = paddedText[i*32 : (i+1)*32]
        for j in range(4):
            word = subString[j*8:(j+1)*8]
            wordArray = [word[k:k+2] for k in range(0,8,2)]
            wordArray = list( map(lambda x: int(x, 16), wordArray) )
            actualBlock.append(wordArray)
        blocks.append(actualBlock)
    return blocks

# Transform text in len(textInHex)/48 blocks of 192 bits each (PKCS5 padding). 
def ECB192(text, encodingType):
    byteText = bytes(text, encoding=encodingType)
    hexByteText = binascii.hexlify(byteText)
    blocks = []
    for i in range(len(hexByteText)//48):
        actualBlock = []
        subString = hexByteText[i*48 : (i+1)*48]
        for j in range(6):
            word = subString[j*8:(j+1)*8]
            wordArray = [word[k:k+2] for k in range(0,8,2)]
            wordArray = list( map(lambda x: int(x, 16), wordArray) )
            actualBlock.append(wordArray)
        blocks.append(actualBlock)
    return blocks
