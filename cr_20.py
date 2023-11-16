
def Fib(n):
    if n > 1:
        a = 1
        b = 1
        k=0
        while k != n-2:
            c = a+b
            a = b
            b = c
            k+=1
        return b
    if n == 1:
        return 1
    else:
        return 'Wrong input format'


n = int(input())
print(Fib(n))