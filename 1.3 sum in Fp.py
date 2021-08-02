# Cộng số nguyên lớn trên trường hữu hạn
from math import*
def convert_array(number,w,t):
  Arr = []
  for i in range(t-1,-1,-1):
    Arr.append(number//2**(w*i))
    number %= 2**(w*i)
  return Arr

def convert_number(Arr,w,t):
  number = 0
  for i in range(t-1,-1,-1):
    number += Arr[t-i-1]*2**(w*i)
  return number
  
def sum(arr_A,arr_B,w,t):
  arr_C = []
  e = 0
  for i in range(t-1,-1,-1):
    c = arr_A[i] + arr_B[i] + e
    e = 0 if 2**w > c >= 0 else 1
    arr_C.append(c%2**w)
  return e,arr_C[::-1]  #reverse arr_C

def sub(arr_A,arr_B,w,t):
  arr_C = []
  e = 0
  for i in range(t-1,-1,-1):
    c = arr_A[i] - arr_B[i] - e
    e = 0 if 2**w > c >= 0 else 1
    arr_C.append(c%2**w) 
  return e,arr_C[::-1]

def sum_Fp(arr_A,arr_B,w,t):
  e, arr_C = sum(arr_A,arr_B,w,t)
  arr_p = convert_array(p,w,t)
  if e == 1:
    return sub(arr_C,arr_p,w,t)
  else:
    if convert_number(arr_C,w,t) > p:
      return sub(arr_C,arr_p,w,t)
  return e,arr_C

A = [int(x) for x in input("Nhap A = ").split()]
B = [int(y) for y in input("Nhap B = ").split()]
w = int(input("Nhap W = "))
p = 2147483647
m = ceil(log(p,2))
t = ceil(m/w)
print(sum_Fp(A,B,w,t))
