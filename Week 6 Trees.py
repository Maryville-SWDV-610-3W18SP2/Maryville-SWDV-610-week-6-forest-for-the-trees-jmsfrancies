from heapq import *
from random import randrange


heap = []
data = []
for i in range (25):
  i  = randrange(1,10)
  total = 15
  if i > 0:
      data.append(i)
      total = total-1
  if data.count(i) >= 2:
      data.remove(i)
  if total == 0:
    print("YES!")
      
for item in data:
   heappush(heap, item)
print(data)
ordered = []
while heap:
   ordered.append(heappop(heap))

ordered
data.sort()
print()
print(data)
data == ordered
True

def Tree(data):
   list = []
   total = 0
   data.reverse()
   print()
   a = '('
   b = ')'
   c = '+'
   d = '/'
   e = '*'
   f = '-'
   while True:
       if len(list) == 0 or len(list)%5 == 0:
         list.append(a)
         list.append(i)
         total = total + 1
       if len(list)%2 == 0: 
         list.append(c)
         list.append(i)
         total = total + 1 
       if len(list)%4 == 0 and list.count(a) >=1: 
          list.append(b)
          list.append(i)
          total = total + 1
       if total == 9:   
          print(list)
          break
Tree(data)    
