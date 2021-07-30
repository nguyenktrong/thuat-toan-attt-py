# kiểm tra số nguyên tố lớn- định lý fermat
from random import randrange

def mod(a,n):
  A = a
  b = 1
  if n-1 == 0:
    return b
  k = bin(n-1)[2:][::-1]
  if k[0] == "1":
    b = a
  for i in range(1,len(k)):
    A = A*A % n
    if k[i] == "1":
      b = b*A % n
  return b

def fermat(n,t):
  for i in range(t):
    a = randrange(2,n-2)
    if mod(a,n) !=1:
      return f"{n} la hop so"
  return f"{n} là snt"

n = int(input("n = "))
t = int(input("t = "))
print(fermat(n,t))
