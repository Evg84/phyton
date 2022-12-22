# Задача 1

week=['понедельник','вторник','среда','четверг','пятница','суббота','воскресенье']
N = int (input())
if N > 7:
  print("такого дня недели не существет")
else :
  if N==1:
    print(week[N-1])
  if N==2:
    print(week[N-1])
  if N==3:
    print(week[N-1])
  if N==4:
    print(week[N-1])
  if N==5:
    print(week[N-1])
  if N==6:
    print(week[N-1])
  if N==7:
    print(week[N-1])   
    
    #Задача 2
    import math

x1=int (input())
y1=int (input())
x2=int (input())
y2=int (input())
round(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2), 2)
   
   # задача 3
   quarter=int (input())
if quarter==1:
  print("x > 0, y > 0")
if quarter==2:
  print("x < 0, y > 0")
if quarter==3:
  print("x < 0, y < 0")
if quarter==4:
  print("x > 0, y < 0")
if quarter>=5:
  print("такой четверти нет,пожалуйста введите от первой четверти до четвёртой четверти")
  
  # Задача 4
  N = int (input())
for i in range(2,N,2):
  print(i)
  j=i
j=j+2
if j==N:
  print(j)
if N<2:
  print("в этом промежутке нет чётных чисел")