# thừa số không tầm thường
def gcd(a,b):
  while b > 0:
    R = a % b
    a = b
    b = R
  return a
def Rho(n):
  a = 2
  b = 2
  for i in range(n):
    a = (a**2 + 1) % n
    b = (b**2 + 1) % n
    b = (b**2 + 1) % n
    d = gcd(a-b, n) 
    if 1 < d < n:
      return f"d = {d}"
    elif d == n:
      return "Math error"

n = int(input("Nhap n = "))
print(Rho(n))
