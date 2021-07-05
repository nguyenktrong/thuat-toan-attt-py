# chuyển mảng thành số - chuyển số thành mảng
from math import *
def convert_array(a,w,t):
  A = []
  for i in range(t-1,-1,-1):
    A.append(a//(2**(i*w)))    
    a=a%(2**(i*w))
  return A
def convert_number(a,w,t):
  number = 0
  for i in range(t-1,-1,-1):
    number += a[t-1-i]*(2**(w*i))  
  return number
w = int(input("Nhap W = "))
p = 2147483647
m = ceil(log(p,2))
t = ceil(m/w)
print("Choose 1 to convert number to array")
print("Choose 2 to convert array to number")
print("Choose 3 to exit")
key = input("Enter: ")
if key == "1":
  a = int(input("Nhap a = "))
  print(f"A = {convert_array(a,w,t)}")
elif key == "2":
  A = [int(a) for a in input("Nhap A = ").split()]
  print(f"a = {convert_number(A,w,t)}")
  
