# kiểm tra số nguyên tố lớn- định lý fermat
from random import randrange
def convertbin(x):
  bin = ""
  while x!=0:
    bin += str(x%2)
    x = x//2
  return bin
def mod(a,n):
  A=a
  b=1
  k = convertbin(n-1)
  if k[0] == '1':
    b=a
  for i in range(1,len(k)):
    A = (A*A) % n  
    if k[i] == '1':    
      b = (b*A) % n
  return b
n = int(input("n = "))
a = randrange(2,n-2)
if mod(a,n)==1:
  print("n là snt")
else:
  print("n là hợp số")
