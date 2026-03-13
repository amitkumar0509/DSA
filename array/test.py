arr = ["hello","hi","I","am","a","python","programmer"]
r = ""
d = ""

for i in arr:
   for j in i[::-1]:
       r += j
   d += r + " "
   r = ""
       
print(d)