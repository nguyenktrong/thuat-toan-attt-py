#phân tích thừa số nguyên tố
def thuasnt(n):
  coso=[]
  somu=[]
  for i in range(2,n):
    cnt = 0
    while n%i == 0:
      n /= i
      cnt = cnt + 1
    if cnt:
      coso.append(i)
      somu.append(cnt)
  return coso,somu
n = int(input("Nhap n = "))
print(f"coso = {thuasnt(n)[0]}, somu = {thuasnt(n)[1]}")
