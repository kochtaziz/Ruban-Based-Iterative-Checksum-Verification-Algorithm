from numpy import *

def puis(x, y):
    p = 1
    for i in range(y):
        p = p * x
    return p

def Ruban(k, d, t):
    ch = str(k)
    l = len(ch) - 1
    for i in range(len(ch)):
        t[i] = puis(10, l) % d
        l = l - 1
    return t

def somme(t, k):
    s = 0
    ch = str(k)
    for i in range(len(ch)):
        s = s + int(t[i]) * int(ch[i])
    return s

def verif(k, d, t):
    if len(str(k)) == 1 and len(str(d)) == 1:
        s = somme(t, k)
    else:
        while len(str(k)) != len(str(d)):
            s = somme(t, k)
            Ruban(k, d, t)
            k = s
    return s == d, k

k = 296419750389
d = 7
t = array([int]*len(str(k)))
Ruban(k, d, t)
print(t)
print(verif(k, d, t))
