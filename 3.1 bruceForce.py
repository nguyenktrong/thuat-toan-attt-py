# đối sánh mẫu-thuật toán vét cạn
def bruceForce(T,P):
  operation = 0
  loop = 0
  for i in range((len(T)-len(P))+1):
    operation += 1
    loop = i
    count = 0
    j = 0
    if P[j] != T[i]:
      continue
    else:
      while P[j] == T[i]:
        count += 1
        i += 1
        j += 1
        if count == len(P):
          return True,loop,operation
        operation += 1
  return False
T = input("Nhap T: ")
P = input("Nhap P: ")
print(bruceForce(T,P))

