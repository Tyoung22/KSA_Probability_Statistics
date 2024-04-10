import random
n = 50
k = 100000
E = 0
for j in range(k):
    x = 0
    for i in range(n):
        x = max(x,random.random())
    E += x
print("MAX : "+str(E/k), n/(n+1))

E = 0
for j in range(k):
    x = 1
    for i in range(n):
        x = min(x,random.random())
    E += x
print("MIN : "+str(E/k))
print(E/k)