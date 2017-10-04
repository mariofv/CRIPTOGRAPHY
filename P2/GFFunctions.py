from fractions import gcd
from random import randint
import time

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


def GF_product_t(a, b, exponencial, logaritme):
    if a == 0 or b == 0:
        return 0
    #[exponencial, logaritme] = GF_tables()
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


[exponencial, logaritme] = GF_tables()
with open('GF_product_p_vs_GF_product_t.txt','w') as f:
    f.write("{:<15}{:<15}{:<30}{:<50}\n".format('a','b',"GF_product_p","GF_product_t"))
    for i in range(1,1000):
        a = randint(0, 255)
        b = randint(0, 255)
        
        start = time.time()
        GF_product_p(a,b)
        end = time.time()
        timeMicroP = (end - start) * 10**6
        
        start = time.time()
        GF_product_t(a,b,exponencial,logaritme)
        end = time.time()
        timeMicroT = (end - start) * 10**6
        
        f.write(("{:<15}{:<15}{:<30}{:<50}\n").format(a,b, timeMicroP, timeMicroT))

f.closed

with open('GF_product_p(a,0x02)_vs_GF_product_t(a,0x02).txt','w') as f:
    f.write("{:<15}{:<15}{:<30}{:<50}\n".format('a','b',"GF_product_p","GF_product_t"))
    [exponencial, logaritme] = GF_tables()
    for i in range(1,1000):
        a = randint(0, 255)
        b = 0x02
        
        start = time.time()
        GF_product_p(a,b)
        end = time.time()
        timeMicroP = (end - start) * 10**6
        
        start = time.time()
        GF_product_t(a,b,exponencial,logaritme)
        end = time.time()
        timeMicroT = (end - start) * 10**6
        
        f.write(("{:<15}{:<15}{:<30}{:<50}\n").format(a,b, timeMicroP, timeMicroT))

f.closed
    
with open('GF_product_p(a,0x03)_vs_GF_product_t(a,0x03).txt','w') as f:
    f.write("{:<15}{:<15}{:<30}{:<50}\n".format('a','b',"GF_product_p","GF_product_t"))
    [exponencial, logaritme] = GF_tables()
    for i in range(1,1000):
        a = randint(0, 255)
        b = 0x03
        
        start = time.time()
        GF_product_p(a,b)
        end = time.time()
        timeMicroP = (end - start) * 10**6
        
        start = time.time()
        GF_product_t(a,b,exponencial,logaritme)
        end = time.time()
        timeMicroT = (end - start) * 10**6
        
        f.write(("{:<15}{:<15}{:<30}{:<50}\n").format(a,b, timeMicroP, timeMicroT))

f.closed

with open('GF_product_p(a,0x09)_vs_GF_product_t(a,0x09).txt','w') as f:
    f.write("{:<15}{:<15}{:<30}{:<50}\n".format('a','b',"GF_product_p","GF_product_t"))
    [exponencial, logaritme] = GF_tables()
    for i in range(1,1000):
        a = randint(0, 255)
        b = 0x09
        
        start = time.time()
        GF_product_p(a,b)
        end = time.time()
        timeMicroP = (end - start) * 10**6
        
        start = time.time()
        GF_product_t(a,b,exponencial,logaritme)
        end = time.time()
        timeMicroT = (end - start) * 10**6
        
        f.write(("{:<15}{:<15}{:<30}{:<50}\n").format(a,b, timeMicroP, timeMicroT))

f.closed

with open('GF_product_p(a,0x0B)_vs_GF_product_t(a,0x0B).txt','w') as f:
    f.write("{:<15}{:<15}{:<30}{:<50}\n".format('a','b',"GF_product_p","GF_product_t"))
    [exponencial, logaritme] = GF_tables()
    for i in range(1,1000):
        a = randint(0, 255)
        b = 0x0B
        
        start = time.time()
        GF_product_p(a,b)
        end = time.time()
        timeMicroP = (end - start) * 10**6
        
        start = time.time()
        GF_product_t(a,b,exponencial,logaritme)
        end = time.time()
        timeMicroT = (end - start) * 10**6
        
        f.write(("{:<15}{:<15}{:<30}{:<50}\n").format(a,b, timeMicroP, timeMicroT))

f.closed

with open('GF_product_p(a,0x0D)_vs_GF_product_t(a,0x0D).txt','w') as f:
    f.write("{:<15}{:<15}{:<30}{:<50}\n".format('a','b',"GF_product_p","GF_product_t"))
    [exponencial, logaritme] = GF_tables()
    for i in range(1,1000):
        a = randint(0, 255)
        b = 0x0D
        
        start = time.time()
        GF_product_p(a,b)
        end = time.time()
        timeMicroP = (end - start) * 10**6
        
        start = time.time()
        GF_product_t(a,b,exponencial,logaritme)
        end = time.time()
        timeMicroT = (end - start) * 10**6
        
        f.write(("{:<15}{:<15}{:<30}{:<50}\n").format(a,b, timeMicroP, timeMicroT))

f.closed

with open('GF_product_p(a,0x0E)_vs_GF_product_t(a,0x0E).txt','w') as f:
    f.write("{:<15}{:<15}{:<30}{:<50}\n".format('a','b',"GF_product_p","GF_product_t"))
    [exponencial, logaritme] = GF_tables()
    for i in range(1,1000):
        a = randint(0, 255)
        b = 0x0E
        
        start = time.time()
        GF_product_p(a,b)
        end = time.time()
        timeMicroP = (end - start) * 10**6
        
        start = time.time()
        GF_product_t(a,b,exponencial,logaritme)
        end = time.time()
        timeMicroT = (end - start) * 10**6
        
        f.write(("{:<15}{:<15}{:<30}{:<50}\n").format(a,b, timeMicroP, timeMicroT))

f.closed



