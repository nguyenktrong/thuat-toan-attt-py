# phép nhân số nguyên lớn
from math import*
def convert_array(a,w,t):
  A = []
  for i in range(t-1,-1,-1):
    A.append(a//(2**(i*w)))    
    a=a%(2**(i*w))
  return A
def multiple(a,b,t):
  C = [0]*(2*t)
  for i in range(t):
    U = 0
    for j in range(t):
      UV = C[i+j] + A[t-1-i]*B[t-1-j] + U
      U = UV // 256
      V = UV % 256
      C[i+j] = V
    C[i+t] = U
  return C[::-1]
p = int(input("p = "))
w = int(input("w = "))
m = ceil(log2(p))
t = ceil(m/w)
print("Choose 1 to multiple two arrays")
print("Choose 2 to multiple two numbers")
key = input("Enter: ")
if key == "1":
  A = [int(a) for a in input("Nhap A = ").split()]
  B = [int(b) for b in input("Nhap B = ").split()]
  print(multiple(A,B,t))
elif key == "2":
  w = int(input("Nhap w = "))
  a = int(input("Nhap a = "))
  b = int(input("Nhap b = "))
  A = convert_array(a,w,t)
  B = convert_array(b,w,t)
  print(multiple(A,B,t))

