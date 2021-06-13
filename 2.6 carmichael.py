# số giả nguyên tố carmichael
from math import gcd
def carmichael(n):
  for a in range(2,n+1):
    if gcd(a,n) == 1:
      if (a**(n-1))%n != 1:
        return False
  return True

n = int(input("Nhap n = "))
print(carmichael(n))
