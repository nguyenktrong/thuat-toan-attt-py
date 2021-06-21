from random import randrange
def convertbin(x):
  bin = ""
  while x!=0:
    bin += str(x%2)
    x = x//2
  return bin
def mod(a,r,n):
  A = a
  b = 1
  k = convertbin(r)
  if k[0] == '1':
    b=a
  for i in range(1,len(k)):
    A = (A*A) % n
    if k[i] == '1':    
      b = (b*A) % n
  return b
def miller_rabin(n):  
  d = n-1
  for i in range(2,n):
    cnt = 0
    while d%i == 0:
      d /= i
      cnt = cnt + 1
    s = cnt
    r = int(d)
    break
  for x in range(t+1):
    a = randrange(2,n-1)
    y = mod(a,r,n)
    if y != 1 and y != (n-1):
      j = 1
      while j <= (s-1) and y != (n-1):
        y = (y*y) % n
        if y == 1:
          return True
        j = j+1
      if y != (n-1):
        return True
  return False
n = int(input("n = "))
t = int(input("t = "))
if miller_rabin(n):
  print(f"{n} la hop so")
else:
  print(f"{n} la so nguyen to")

