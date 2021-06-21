# đối sánh mẫu-thuật toán vét cạn
def bruceForce(T,P):
  operation = 0 # tính số phép toán
  loop = 0 # tính số vòng lặp
  for i in range((len(T)-len(P))+1):
    operation += 1
    loop += 1
    count = 0 # đếm số ký tự bằng nhau 
    j = 0
    while P[j] == T[i+j]:
      count += 1
      j += 1
      if count == len(P):
        return True, loop, operation
      operation += 1
  return False, loop, operation

T = input("Nhap T: ")
P = input("Nhap P: ")
if bruceForce(T, P)[0]:
  print(f"P xuat hien o vi tri {bruceForce(T, P)[1]-1}") # loop -1
  print(f"so vong lap = {bruceForce(T,P)[1]}") # loop
  print(f"so phep toan = {bruceForce(T,P)[2]}") # operation
else:
  print("P khong xuat hien trong T ")
  print(f"so vong lap = {bruceForce(T,P)[1]}") # loop
  print(f"so phep toan = {bruceForce(T,P)[2]}") # operation



