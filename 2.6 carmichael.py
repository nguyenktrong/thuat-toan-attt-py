# số giả nguyên tố carmichael
from math import sqrt,gcd
def prime(n):
  for i in range(2, int(sqrt(n))):
    if n%i == 0:
      return False
  return True

def carmichael(n):
  if prime(n):
    return False
  else:
    for a in range(2, n+1):
      if gcd(a, n) == 1:
        if (a**(n-1))%n != 1:
          return False
    return True

n = int(input("Nhap n = "))
print(carmichael(n))

