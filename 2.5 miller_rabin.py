from random import randrange

def mod(a,n,r):
  A = a
  b = 1
  if r == 0:
    return b
  k = bin(r)[2:][::-1]
  if k[0] == "1":
    b = a
  for i in range(1,len(k)):
    A = A*A %n
    if k[i] == "1":
      b = A*b % n
  return b

def miller_rabin(n,t):
  d = n-1
  for i in range(2,n):
    cnt = 0
    while n%i == 0:
      cnt += 1
      d /= i
    s = cnt
    r = int(d)
    break
  for i in range(t):
    a = randrange(2,n-1)
    y = mod(a,n,r)
    if y != 1 and y != n-1:
      j=1
      while j <= s-1 and y != n-1:
        y = y*y % n
        if y == 1:
          return f"{n} la hop so"
        j += 1
      if y != n-1:
        return f"{n} la hop so" 
  return f"{n} la so nguyen to"

n = int(input("Nhap n = "))
t = int(input("Nhap t = "))
print(miller_rabin(n,t))




