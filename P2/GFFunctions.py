from fractions import gcd

def multPerX(a):
    result = (a << 1)&0xFF
    if a&0x80:
        result = result^0x1B
    return result

def GF_product_p(a, b):
    if a == 0 or b == 0:
        return 0
    result = 0;
    for i in range(0,8):
        if b&0x01:
            sumaParcial = a
            for j in range(0,i):
                sumaParcial = multPerX(sumaParcial)
            result = result^sumaParcial
        b = b>>1
    return result


def GF_tables():
    exponencial = [None] * 256
    logaritme = [None] * 256
    lastElement = 0x01
    for i in range(1,256):
        lastElement = GF_product_p(0x03,lastElement);
        exponencial[i] = lastElement 
        logaritme[lastElement] = i
    return (exponencial, logaritme)


def GF_product_t(a, b):
    if a == 0 or b == 0:
        return 0
    [exponencial, logaritme] = GF_tables()
    return exponencial[(logaritme[a] + logaritme[b])%256]
        
def GF_generador():
    generadors = []
    [exponencial, logaritme] = GF_tables()
    for i in range(1, len(exponencial)):
        if gcd(i,255) == 1:
            generadors.append(exponencial[i])
    return generadors

def GF_invers(a):
    if a == 0:
        return 0
    [exponencial, logaritme] = GF_tables()
    return exponencial[255-logaritme[a]]

