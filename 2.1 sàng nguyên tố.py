#thuật toán sàng nguyên tố Eratosthenes
def snt(n):
  check=[True]*(n+1)
  s=[]
  for i in range(2,n+1):
    if check[i]:
      for j in range(i*i,n+1,i):
        check[j]=False
      s.append(i)
  return s
n=int(input('Nhap n = '))
print(snt(n))
