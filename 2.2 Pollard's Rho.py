import math
def gcd(a,b):
  A=a
  B=b
  while B>0:
    R=A%B
    A=B
    B=R
  return A
def Rho(n):
  a=2
  b=2
  for i in range(n):
    a=(a*a+1)%n
    b=(b*b+1)%n
    b=(b*b+1)%n
    d=math.gcd(a-b,n)
    if n > d > 1:
      return d,n/d
    if n == d:
      return False
n=int(input("Nhap n = "))
print(f"d = {Rho(n)[0]}")
