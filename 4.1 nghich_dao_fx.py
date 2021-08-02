def sum(f,g):
  if len(f)>=len(g):
    result = f
    space = len(f) - len(g)
    for i in range(len(g)):
      result[i+space] = (f[i+space] + g[i]) % 2
  else:
    result = g
    space = len(g) - len(f)
    for i in range(len(f)):
      result[i+space] = (g[i+space] + f[i]) % 2
  while result and result[0] == 0:
    result.remove(result[0])
  return result 
#
def sub(f,g):
  return sum(f,g)
#
def mul_x(f,c):
  result_x = []
  for i in range(len(f)):
    result_x.append(f[i]*c)
  return result_x
#
def mul(f,g):
  result = [0]*(len(g))
  for i in range(len(f)):
    if i < len(f)-1:
      sum(result,mul_x(g,f[i])).append(0)
    else:
      sum(result,mul_x(g,f[i]))
  return result

def div(f,g):
  result_div = []
  for i in range(len(f)):
    result_div.append(int(f[0]/g[0]))
    t = mul([1],g)
    #print("t = ",t)
    while len(t)<len(f):
      t.append(0)
    f = sub(f,t)
    #print("f = ",f)
    if len(f) < len(g):
      return result_div
    #print("result = ",result_div)
    #print("g = ",g)
    #print("---")
def euclide(f,g):
  x2=[1]
  x1=[0]
  y2=[0]
  y1=[1]
  while(g[0] != 0):
    q=div(f,g)
    print(q, end = "  ")
    r=sub(f,mul(q,g))
    print(r, end = "  ")
    x=sub(x2-mul(q,x1))
    print(x, end = "  ")
    y=sub(y2-mul(q,y1))
    print(y, end = "  ")
    f = g
    print(f, end = "  ")
    g = r
    print(g, end = "  ")
    x2=x1
    print(x2, end = "  ")
    x1=x
    print(x1, end = "  ")
    y2=y1
    print(y2, end = "  ")
    y1=y
    print(y1, end = "  ")
  d=f
  x=x2
  y=y2
  return d,x,y
f = [int(x) for x in input("Nhap f = ").split()]
g = [int(y) for y in input("Nhap g = ").split()]
print(euclid(f,g))
'''f = [1, 0, 1, 1]
g = [1, 1, 1]
#print(div(f,g))
q = mul(div(f,g),g)
print(q)
print(len(q))
print(sub(f,f))
#(euclide(f,g))
#print(sub(f,g))'''
