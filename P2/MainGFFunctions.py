import time
import sys
from random import randint
from GFFunctions import *

with open('./out/GF_product_p_vs_GF_product_t.txt','w') as f:
    f.write("{:<15}{:<15}{:<30}{:<50}\n".format('a','b',"GF_product_p","GF_product_t"))
    for i in range(1,1000):
        a = randint(0, 255)
        b = randint(0, 255)
        
        start = time.time()
        GF_product_p(a,b)
        end = time.time()
        timeMicroP = (end - start) * 10**6
        
        start = time.time()
        GF_product_t(a,b)
        end = time.time()
        timeMicroT = (end - start) * 10**6
        
        f.write(("{:<15}{:<15}{:<30}{:<50}\n").format(a,b, timeMicroP, timeMicroT))

f.closed

with open('./out/GF_product_p(a,0x02)_vs_GF_product_t(a,0x02).txt','w') as f:
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
        GF_product_t(a,b)
        end = time.time()
        timeMicroT = (end - start) * 10**6
        
        f.write(("{:<15}{:<15}{:<30}{:<50}\n").format(a,b, timeMicroP, timeMicroT))

f.closed
    
with open('./out/GF_product_p(a,0x03)_vs_GF_product_t(a,0x03).txt','w') as f:
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
        GF_product_t(a,b)
        end = time.time()
        timeMicroT = (end - start) * 10**6
        
        f.write(("{:<15}{:<15}{:<30}{:<50}\n").format(a,b, timeMicroP, timeMicroT))

f.closed

with open('./out/GF_product_p(a,0x09)_vs_GF_product_t(a,0x09).txt','w') as f:
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
        GF_product_t(a,b)
        end = time.time()
        timeMicroT = (end - start) * 10**6
        
        f.write(("{:<15}{:<15}{:<30}{:<50}\n").format(a,b, timeMicroP, timeMicroT))

f.closed

with open('./out/GF_product_p(a,0x0B)_vs_GF_product_t(a,0x0B).txt','w') as f:
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
        GF_product_t(a,b)
        end = time.time()
        timeMicroT = (end - start) * 10**6
        
        f.write(("{:<15}{:<15}{:<30}{:<50}\n").format(a,b, timeMicroP, timeMicroT))

f.closed

with open('./out/GF_product_p(a,0x0D)_vs_GF_product_t(a,0x0D).txt','w') as f:
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
        GF_product_t(a,b)
        end = time.time()
        timeMicroT = (end - start) * 10**6
        
        f.write(("{:<15}{:<15}{:<30}{:<50}\n").format(a,b, timeMicroP, timeMicroT))

f.closed

with open('./out/GF_product_p(a,0x0E)_vs_GF_product_t(a,0x0E).txt','w') as f:
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
        GF_product_t(a,b)
        end = time.time()
        timeMicroT = (end - start) * 10**6
        
        f.write(("{:<15}{:<15}{:<30}{:<50}\n").format(a,b, timeMicroP, timeMicroT))

f.closed






        
        
 
