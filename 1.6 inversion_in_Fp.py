# tính nghịch đảo trên Fp
p = int(input("p = "))
a = int(input("a = "))
def exteuclid(a,p):
  u = a
  v = p
  x1 = 1
  x2 = 0
  while u != 1:
    q = v//u
    r = v%u
    x = x2 - q*x1
    v = u
    u = r
    x2 = x1
    x1 = x
  return x1%p
print(exteuclid(a,p))
