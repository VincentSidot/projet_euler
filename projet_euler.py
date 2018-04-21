## Probleme 12

def list_divisor(n):
    divisor = [1]
    divisor2 = [n]
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            divisor += [i]
            if i !=int(n**0.5):
                divisor2 += [int(n/i)]
    return divisor + list(reversed(divisor2))

def count_divisor(n):
    divisor = 2
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            divisor += 1
            if i !=int(n**0.5):
                divisor += 1
    return divisor
    
def problem12():
    divisor = 0
    i,triangular = 0,0
    while divisor < 500:
        i+=1
        triangular+=i
        divisor = count_divisor(triangular)
    return i
    
## Problem 38

def D2B(n,B=10):
    L = []
    while n > 0:
        L = [n%B] + L
        n//=B
    return L

def fastpow(x,n):
    if n==0:
        return 1
    elif n%2==0:
        return fastpow(x,n//2)*fastpow(x,n//2)
    else:
        return fastpow(x,n//2)*fastpow(x,n//2)*x
        
pow5 = [fastpow(i,5) for i in range(10)]

def fifthDigitSum(n):
    rep = 0
    while n>0:
        rep += pow5[n%10]
        n//=10
    return rep

def problem38():
    rep = 0
    for i in range(10,10**6):
        if i == fifthDigitSum(i):
            rep += i
    return rep

## Problem 31

p = [1,2,5,10,20,50,100,200]

def problem31():
    rep = 0
    for x1 in range(201):
        if x1>200:
            break
        for x2 in range(101):
            if x1+2*x2>200:
                    break
            for x3 in range(41):
                if x1+2*x2+5*x3>200:
                    break
                for x4 in range(21):
                    if x1+2*x2+5*x3+10*x4>200:
                        break
                    for x5 in range(11):
                        if x1+2*x2+5*x3+10*x4+20*x5>200:
                            break
                        for x6 in range(5):
                            if x1+2*x2+5*x3+10*x4+20*x5+50*x6>200:
                                break
                            for x7 in range(3):
                                if x1+2*x2+5*x3+10*x4+20*x5+50*x6+100*x7>200:
                                    break
                                for x8 in range(2):
                                    if x1+2*x2+5*x3+10*x4+20*x5+50*x6+100*x7+200*x8>200:
                                        break
                                    if x1+2*x2+5*x3+10*x4+20*x5+50*x6+100*x7+200*x8==200:
                                        rep+=1
    return rep

## Problem 27
""" b as to be prime"""

def crible(n):
    P = [0,0] + list(range(2,n))
    for i in range(2,int(n**0.35)+1):
        if P[i] != 0:
            for j in range(2*i,n,i):
                P[j] = 0
    return [p for p in P if p!=0]

def isPrime(n):
    if n <= 0 or n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

B = crible(1000)
A = range(-1000,1001)

def problem27():
    max,amax,bmax = 0,0,0
    for a in A:
        for b in B:
            n = 0
            while isPrime(n*n+a*n+b):
                n+=1
            if n > max:
                amax,bmax=a,b
                max = n
    return amax*bmax
    
## Problem 21

def properDivisor(n,extremum=False):
    if extremum:
        L = [1,n]
    else:
        L = []
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            L+=[i]
            if i != n/2:
                L+=[n//i]
    #L.sort()
    return L

def d(n):
    return sum(properDivisor(n))+1


def problem21():
    rep = 0
    for a in range(1,10000):
        b = d(a)
        if d(b)==a and b!=a:
           rep += a 
    return rep

## Problem 24 

L = [0,1,2]

def fact(n):
    rep = 1
    for i in range(2,n+1):
        rep*=n
    return rep

def Permutation(L):
    return
    
## Problem 22

file = open("problem22.txt",'r')

def strToList(str):
    L = []
    word = ""
    for i in str:
        if ord(i)>=ord('A') and ord(i) <= ord('Z'):
            word += i
        else:
            if len(word)>0:
                L += [word]
            word = ""
    if len(word)>0:
        L += [word]
    return L

def pound(word):
    rep = 0
    for i in word:
        rep += ord(i)-ord('A')+1
    return rep
    
rep = 0
L = strToList(file.read())
L.sort()
for i in range(len(L)):
    rep += pound(L[i])*(i+1)
print(rep)

## Problem 17

usual = { 1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',100:'hundred',1000:'thousand',1000000:'million'}

def number_to_str(n):
    if n <= 0:
        return "error"
    if n <= 20:
        return usual[n]
    if n/10 == n//10 and n<100:
        return usual[n]
    if n > 20 and n < 100:
        dec = n//10
        unit = n%10
        return number_to_str(10*dec) + '-' + number_to_str(unit)
    if n/100 == n//100 and n<1000:
        return number_to_str(n//100) + " " + usual[100]
    if n > 100 and n < 1000:
        cent = n//100
        rest = n%100
        return number_to_str(cent*100) + " and " + number_to_str(rest)
    if n/1000 == n//1000 and n<1000000:
        return number_to_str(n//1000) + " " + usual[1000]
    if n > 1000 and n < 1000000:
        mille = n//1000
        rest = n%1000
        return number_to_str(mille*1000) + ' ' + number_to_str(rest)
    if n/1000000 == n//1000000 and n<1000000000:
        return number_to_str(n//1000000) + " " + usual[1000000]
    if n > 1000000 and n < 1000000000:
        million = n//1000000
        rest = n%1000000
        return number_to_str(million*1000000) + ' ' + number_to_str(rest)
    return 'error'

def count_number(word):
    rep = 0
    for i in word:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            rep+=1
    return rep
def problem17():
    rep = 0
    for i in range(1,1001):
        rep += count_number(number_to_str(i))
    print(rep)

## Problem 15

def fact(n):
    for i in range(1,n):
        n*=i
    return n

def binom(k,n): # implementation merdique
    return fact(n)//(fact(k)*fact(n-k))
    
## Problem 18

M = [3,7,4,2,4,6,9,5,9,3]


def string_to_list(str):
    L = []
    word = ""
    for i in str:
        if ord(i)>=ord('0') and ord(i)<=ord('9'):
            word += i
        else:
            if len(word)>0:
                L+=[int(word)]
            word = ""
    if len(word)>0:
        L+=[int(word)]
    return L

str = "75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 88 02 77 73 07 63 67 99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 04 68 89 53 67 30 73 16 69 87 40 31 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"

def triangular(n):
    return (n*(n+1))//2

def trouver_hauteur(x):
    i = 0
    while x>triangular(i):
        i+=1
    return i

def reduce_path(L):
    h = trouver_hauteur(len(L))
    newL = L[:len(L)-h]
    a = triangular(h-2)
    b = triangular(h-1)
    for i in range(h-1):
        newL[a+i] += max(L[b+i],L[b+i+1])
    return newL
    
def find_max_path(L):
    while len(L) > 1:
        L = reduce_path(L)
    return L[0]
    
## Problem 29

def fastpow(x,n):
    if n == 0:
        return 1
    if n%2==0:
        return pow(x,n//2)*pow(x,n//2)
    else:
        return pow(x,n//2)*pow(x,n//2)*x

def gen(a,b):
    L = []
    for i in range(2,a+1):
        for j in range(2,b+1):
            L += [fastpow(i,j),fastpow(j,i)]
    L.sort()
    return L

def singularise(L):
    rep = []
    for i in L:
        if i not in rep:
            rep += [i]
    return rep
    
## Problem 69

def crible(n):
    P = [0,0] + list(range(2,n))
    for i in range(2,int(n**0.5)+1):
        if P[i] != 0:
            for j in range(2*i,n,i):
                P[j] = 0
    return [p for p in P if p!=0]
    
Prime = crible(1000000)

def PrimeFactor(n):
    L = []
    for p in Prime:
        while n%p == 0:
            L+=[p]
            n//=p
    return L
def f(n):
    rep = 1
    for p in PrimeFactor(n):
        rep *= 1-(1/p)
    return 1/rep

## Problem 26
import matplotlib.pyplot as plt

def fastpow(x,n):
    if n == 0:
        return 1
    if n%2==0:
        return pow(x,n//2)*pow(x,n//2)
    else:
        return pow(x,n//2)*pow(x,n//2)*x

def checkOccurence(n,L):
    for i in range(len(L)):
        if L[i]==n:
            return i
# NON FONCTIONEL sauf pour les nombre premier
def lenCycle(n):
    L = []
    i = 0

    while  True:
        p = int(fastpow(10,i)//n)
        if p!=0:
            if p%10 == 0:
                return 0
            if p%10 in L:
                return i-checkOccurence(p%10,L)-1
            L += [p%10]
        i+=1

def problem26():
    max,imax = 0,0
    for i in range(1,1000):
        p = lenCycle(i)
        if p > max:
            max,imax = p,i
    return max,imax

def plot():
    X = range(1,1000)
    Y = [lenCycle(i) for  i in X]
    plt.plot(X,Y)
    plt.grid(True)
    plt.show()

## Problem 32

def D2B(n,B=10):
    L = []
    while n > 0:
        L = [n%B] + L
        n//=B
    return L
    
def isPandigital(n,onlyOnce = True):
    Appear = [False]*9
    L = D2B(n)
    if len(L)<9:
        return False
    for i in L:
        if i != 0:
            if onlyOnce and Appear[i-1]:
                return False
            Appear[i-1] = True
    for j in Appear:
        if not j:
            return False
    return True