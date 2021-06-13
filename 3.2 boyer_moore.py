# đối sánh mẫu-Thuật toán boyer_moore 
def pre(T, P, i, j):
  i = i + len(P) - min(j, 1 + P.rfind(T[i]) )
  j = len(P) - 1
  return i, j

def boyer_moore(T, P):
  i = len(P) - 1
  j = len(P) - 1
  count = 0
  loop = 0
  operation = 0
  while i < len(T) - 1:
    loop += 1
    operation += 1
    while(P[j] == T[i]):
      count += 1
      i -= 1
      j -= 1
      if count == len(P):
        return True,loop,operation
      operation += 1
    i,j = pre(T, P, i, j)
  return False,loop,operation
T = input("Nhap T: ")
P = input("Nhap P: ")
if boyer_moore(T,P)[0]:
  print("P is in T ")
  print(f"so vong lap = {boyer_moore(T,P)[1]}")
  print(f"so phep toan = {boyer_moore(T,P)[2]}")
else:
  print("P isn't in T ")
  print(f"so vong lap = {boyer_moore(T,P)[1]}")
  print(f"so phep toan = {boyer_moore(T,P)[2]}")
