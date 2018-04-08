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

## Problem 19
