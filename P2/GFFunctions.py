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
    exponencial = [None for x in range(255)]
    logaritme = [None for x in range(256)]
    lastElement = 0x01
    for i in range(255):
        lastElement = GF_product_p(0x03,lastElement);
        exponencial[i] = lastElement 
        logaritme[lastElement] = i
    return (exponencial, logaritme)


[exponencial, logaritme] = GF_tables()

def GF_product_t(a, b):
    if a == 0 or b == 0:
        return 0
    global exponencial, logaritme
    return exponencial[(logaritme[a] + logaritme[b] + 1)%255]
        
def GF_generador():
    generadors = []
    global exponencial, logaritme
    for i in range(len(exponencial)):
        if gcd(i+1,255) == 1:
            generadors.append(exponencial[i])
    return generadors

def GF_invers(a):
    if a == 0:
        return a
    global exponencial, logaritme
    return exponencial[254-(logaritme[a]+1)]
