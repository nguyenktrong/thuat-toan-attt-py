# Cộng số nguyên lớn trên trường hữu hạn
from math import *
def convert_array(a,w,t):
  A = []
  for i in range(t):
    A.append(a//(2**((t-i-1)*w)))
    a = a % (2**((t-i-1)*w))
  return A

def convert_number(A,w,t):
  number = 0
  for i in range(t-1,-1,-1):
    number += A[t-1-i]*(2**(w*i))
  return number

def sum(A,B,w,t):
  C = []
  e = 0
  for i in range(t-1,-1,-1):
    c = A[i] + B[i] + e
    if 0 <= c < 2**w:
      e = 0
    else:
      e = 1
    C.append(c%(2**w))
  return e,C[::-1]

def subtract(A,B,w,t):
  C = []
  e = 0
  for i in range(t-1,-1,-1):
    c = A[i] - B[i] - e
    if 0 <= c < 2**w:
      e = 0
    else:
      e = 1
    C.append(c%(2**w))
  return e,C[::-1]
def sumFp(A,B,w,t):
  if sum(A, B, w, t)[0] == 1:
    return subtract(sum(A, B, w, t)[1], convert_array(p, w, t), w, t)
  else:
    if convert_number(sum(A,B,w,t)[1],w,t) > p:
      return subtract(sum(A, B, w, t)[1], convert_array(p, w, t), w, t)
    return sum(A, B, w, t)
w = int(input("Nhap W = "))
p = 2147483647
m = ceil(log(p,2))
t = ceil(m/w)
A = [int(a) for a in input("Nhap A = ").split()]
B = [int(b) for b in input("Nhap B = ").split()]
print(sumFp(A,B,w,t))

