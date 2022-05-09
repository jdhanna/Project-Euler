import time


def evenFibSum(cap):
    ans = 0
    a= 1
    b = 1
    while b < cap:
        c = a + b
        a = b
        b = c
        if b%2 == 0:
            ans += b
    return ans


def fibNextEven(a, b):
    return 4*b + a

def fastEvenFibSum(cap):
    ans = 10
    a = 2
    b = 8
    c = 34
    while c < cap:
        ans += c
        a = b
        b = c
        c = fibNextEven(a, b)
    return ans

start = time.time()
#print(evenFibSum(4000000))
#mid = time.time()
print(fastEvenFibSum(4000000))
end = time.time()
