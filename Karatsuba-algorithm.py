'''Вход: два л-значных неотрицательных целых числа, х и у. Выход: произведение х х у.'''
import time
import string
import math

start = time.time()
def fourDigit(v):
    num = input("Введите "+v+"= 4-х значное число: ")
    # if len(num) == 4 and num.isdigit():
    if len(num) >= 4:
        print("Принято", num)
        return num
    else:
       print("Ощибка!!!")
       fourDigit(v)

def RectIntMult(x,y):
    if len(x)==1 or len(y)==1:
        return int(x)*int(y)
    else:
        m = min(len(x), len(y))
        m1=math.ceil(len(x)/2)
        m2=math.ceil(len(y)/2)
        a,b=x[:m1],x[m1:]
        print(a,b)
        c,d=y[:m2],y[m2:]
        print(c,d)

        z0 = int(RectIntMult(b,d))
        z1 = int( RectIntMult(str(int(b)+int(a)),str(int(d)+int(c))))
        z2 = int(RectIntMult(a, c))
        return ((10**(m))*z2)+((10**(m/2))*(z1-z2-z0))+z0

# def RectIntMult(x,y):
#     try:
#         n1=len(x)
#         n2=len(y)
#         if n1==1 or n2==1:
#             print("n=1")
#             sum = int(x)*int(y)
#         else:
#             print("n>1")
#             a = int(x[:n1//2])
#             b = int(x[n1//2:])
#             c = int(y[:n2//2])
#             d = int(y[n2//2:])
#             p=a+b
#             q=c+d
#             ac=a*c
#             bd=b*d
#             pq=p*q
#             abdc=pq-ac-bd
#             sum=(10**n1*ac)+((10**(n1/2)))*(abdc)+bd
#     finally:
#         return sum

def main():
    x=str(fourDigit('x'))
    y=str(fourDigit('y'))
    sum=RectIntMult(x,y)
    print('x * y = ',sum)
    end = time.time() - start
    print('время: ',end)

if __name__ == "__main__":
    main()
