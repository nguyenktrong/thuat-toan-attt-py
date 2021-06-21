# đối sánh mẫu - thuật toán kruth morris pratt
def preKMP(P, j):
  if j == 0:
    return -1  # <-> F[0] = -1 
  for i in range(len(P)):
   '''so sánh tiền tố dài nhất với hậu tố dài nhất
      nếu không khớp giảm dần
   ex: P = "abacab"
       P[0:2] = aba -> P[0:1] = ab -> P[0:0] = a
       P[1:3] = bac -> P[2:3] = ac -> P[3:3] = a => F[3] = 1
   '''
    if P[0: j-1-i] == P[1+i: j]:  
      j_new = len( P[0: j-1-i])   # <-> F[j] = độ dài tiền tố dài nhất
      return j_new
    j_new = 0 # xâu rỗng -> F[j] = 0
  return j_new # <-> trả về F[j]
def KMP(T,P):
  i = 0
  j = 0
  loop = 0 # số vòng lặp
  operation = 0 # số phép toán
  while i < len(T)-len(P):
    loop += 1
    operation += 1
    count = 0 # đếm số ký tự khớp
    while P[j] == T[i+j]:
      count += 1
      if count == len(P):
        return True, loop, operation, i
      j += 1
      operation += 1    
    i = i + j - preKMP(P, j)
    j = 0 if preKMP(P, j) == -1 else preKMP(P, j)
  return False, loop, operation
T = input("Nhap T: ")
P = input("Nhap P: ")
if KMP(T,P)[0]:
  print(f"P xuat hien trong T o vi tri {KMP(T,P)[3]}") #i
  print(f"so vong lap: {KMP(T,P)[1]}") # loop
  print(f"so phep tinh: {KMP(T,P)[2]}") # operation
else:
  print("P khong xuat hien trong T")
  print(f"so vong lap: {KMP(T,P)[1]}") # loop
  print(f"so phep tinh: {KMP(T,P)[2]}") #operation
