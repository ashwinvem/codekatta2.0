ls = list(map(int,input().split()))
min = ls[0]
for i in ls:                                                  min num in array
    if min > i:
        min = i
print(min)
--------------------------------------------------------
n , m = list(map(int,input().split()))
ls = list(map(int,input().split()))
count = -1
for i in ls:                                         print how many times given int repeated in array
    if m == i:
        count += 1
print(count)
------------------------------------------------------------
a = int(input())
m , n = list(map(int,input().split()))
count = 0
for i in range(m,n):
    if i == a:
        count += 1
if count > 0:                                              check given int presented in arrray r not
    print('yes')                                                  
else:
    print('no')
---------------------------------------------------------
m , n = list(map(int,input().split()))
while m != n:
    if m > n:
        m -= n                                                   gcd
    else:
        n -= m
print(m)
-----------------------------------------
import math
m , n = list(map(int,input().split()))
a = m * n
b = a**0.5
if b - math.floor(b) == 0:
    print('yes')                                                      perfect square r not
else:
    print('no')
----------------------
n = int(input())
ls = list(map(int,input().split()))
for i in range(0,n,2):
    if i + 1 == n:                                                    adjacent ints swap
        break
    temp = ls[i]
    ls[i] = ls[i+1]
    ls[i+1] = temp
for i in ls:
    print(i,end=' ')

15
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
2 1 4 3 6 5 8 7 10 9 12 11 14 13 15

----------------------------------------------------
n = int(input())
sum = 0
for i in range(n+1):
    sum += i                                                                            sum of array ints
print(sum)
---------------------------------------------------
m, n, k = list(map(int,input().split()))
if m != n and n != k and m!=k:
    print('yes')                                            check whther scalene triangle r not
else:
    print('no')

scalene traingle no sides should be equal
----------------------------------------

def factorial(n):
    if n <=1:
        return 1
    else:
        return n*factorial(n-1)                                          factorial
n = int(input())
print(factorial(n))
-------------------------------------------
m , n, k = list(map(int,input().split()))
a = m**2 + n**2
b = k**2
if a==b:
    print('yes')                                                           whther right angle triangle r not
else:
    print('no')
-------------------------------------------------
m , n = list(map(int,input().split()))
a = m+n                                                                     eeven r odd
if a %2 ==0:
    print('even')
else:
    print('odd')
---------------------------------------------------
m, n = list(map(int,input().split()))
ls = list(map(int,input().split()))                                     given int is exist in array r not
if n in ls:
    print('yes')
else:
    print('no')
--------------------------------------------
n = int(input())
ls = list(map(int,input().split()))
min = ls[0]
max = ls[0]
for i in ls:
    if min > i:                                            max n min in array
        min = i
    elif max < i:
        max = i
print(min,end=' ')
print(max,end=' ')
5
5 6 4 9 9
4 9     min n max
-----------------------------------------------------------
st = input()
st1=''
a = st.split(' ')
for i in a:
    st1 = i +' '+ st1
print(st1)                                                                string word reverse
string reverse
hlo world hi
 hi world hlo
----------------------------------------------------------
p1 = list(map(int,input().split()))
p2 = list(map(int,input().split()))
p3 = list(map(int,input().split()))
p4 = list(map(int,input().split()))

def square(p1,p2):
    a = (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2
    b = abs(a)
    # print(b)
    return b                                                        square r not
a = square(p1,p2)
b = square(p2,p3)
c = square(p3,p4)
d = square(p4,p1)
e = square(p3,p1)
if a==b==c==d and a+b == e:
    print('yes')
else:
    print('no')

points r square root r not
--------------------------------------------------------

str = input()   method1
print(''.join([str[x:x+2][::-1] for x in range(0,len(str),2)]))

str = list(input())
for i in range(0,len(str),2):                                        swap odd to even positions
    if i+1 == len(str):
        break
    temp = str[i]
    str[i] = str[i+1]
    str[i+1]= temp
for i in str:
    print(i,end='')        method 2
---------------------------------------------------
n = int(input())
count = 0
for i in range(1,10):
    if n%i==0:
        count = i
if count > 1:
    print('yes')
else:                                                        composite num ?
    print('no')
