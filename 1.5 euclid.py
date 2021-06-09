# tính nghịch đảo bằng euclid
def euclide(a,b):
  if b == 0:
    d=a
    x=1
    y=0
  else:
    x2=1
    x1=0
    y2=0
    y1=1
    while(b>0):
      q=a//b
      r=a%b
      x=x2-q*x1
      y=y2-q*y1
      a=b
      b=r
      x2=x1
      x1=x
      y2=y1
      y1=y
    d=a
    x=x2
    y=y2
  return d,x,y
a,b = [int(x) for x in input("Nhap a,b = ").split()]
print(euclide(a,b))
