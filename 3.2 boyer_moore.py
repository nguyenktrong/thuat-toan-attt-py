# đối sánh mẫu-Thuật toán boyer_moore 
def preBM(T, P, i, j):
  i = i + len(P) - min(j, 1 + P.rfind(T[i])) # hàm P.rfind(T[i]): tìm chỉ số cao nhất của T[i] trong P 
  j = len(P) - 1
  return i, j

def boyer_moore(T, P):
  i = len(P) - 1
  j = len(P) - 1
  loop = 0 # tính số vòng lặp
  operation = 0 # tính số phép toán
  while i < len(T) - 1:
    count = 0
    loop += 1
    operation += 1
    while(P[j] == T[i]):
      count += 1
      if count == len(P):
        return True, loop, operation,i
      i -= 1
      j -= 1
      operation += 1
    i, j = preBM(T, P, i, j)
  return False, loop, operation
  
T = input("Nhap T: ")
P = input("Nhap P: ")
if boyer_moore(T, P)[0]:
  print(f"P xuat hien o vi tri {boyer_moore(T, P)[3]}") 
  print(f"so vong lap = {boyer_moore(T, P)[1]}")
  print(f"so phep toan = {boyer_moore(T, P)[2]}")
else:
  print("P khong xuat hien trong T ")
  print(f"so vong lap = {boyer_moore(T, P)[1]}")
  print(f"so phep toan = {boyer_moore(T, P)[2]}")
