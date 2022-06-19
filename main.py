#A
#1.The program gives correct output only when only one of 3 given numbers is odd or all the given 3 numbers are even
#2.when the elif statement is replaced with if condition. Use 3 if conditions to work the code properly.
#3. We can use ternary operator instead of if-else statement.


def count(n1,n2,n3):
    a = 1 if n1%2!=0 else 0
    b=1 if n2%2!=0 else 0
    c= 1 if n3%2!=0 else 0
    count = a+b+ c
print(count)
#B.
def count_factors(n):
    count=0
    for num in range(0,n+1):
        if n%num==0:
        count++
    return count

#c
def replace_all( wordlist, target, replace):
    for i in range(len(wordlist)):
        if wordlist[i] == target:
    wordlist[i] = replace

#D
def rotate_left(l):
    m=l[:]
    n=len(l)
    for i in range(0,n-1):
    l[i]=m[i+1]
    l[n-1]=m[0]