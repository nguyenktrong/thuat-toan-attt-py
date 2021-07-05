# Thuật toán cộng - trừ chính xác bội
from math import *
def convert_array(a,w,t):
  A = []
  for i in range(t):
    A.append(a//(2**((t-i-1)*w)))    
    a = a % (2**((t-i-1)*w))
  return A

def sum(a,b,w,t):
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
def subtraction(a,b,w,t):
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

# phép cộng trừ số nguyên lớn
w = int(input("Nhap W = "))
p = 2147483647
m = ceil(log(p,2))
t = ceil(m/w)
print("Choose 1 to sum")
print("Choose 2 to subtract")
key = input("Enter: ")
if key == "1":
  print("Choose a to sum two arrays")
  print("Choose b to sum two numbers")
  newkey = input("Enter: ")
  if newkey == "a":  
    A = [int(a) for a in input("Nhap A = ").split()]
    B = [int(b) for b in input("Nhap B = ").split()]
    print(sum(A,B,w,t))
  elif newkey == "b":
    a = int(input("Nhap a = "))
    b = int(input("Nhap b = "))
    A = convert_array(a,w,t)
    B = convert_array(b,w,t)
    print(sum(A,B,w,t))
elif key == "2":
  print("Choose a to subtract two arrays")
  print("Choose b to subtract two numbers")
  newkey = input("Enter: ")
  if newkey == "a":  
    A = [int(a) for a in input("Nhap A = ").split()]
    B = [int(b) for b in input("Nhap B = ").split()]
    print(subtraction(A,B,w,t))
  elif newkey == "b":
    a = int(input("Nhap a = "))
    b = int(input("Nhap b = "))
    A = convert_array(a,w,t)
    B = convert_array(b,w,t)
    print(subtraction(A,B,w,t))
