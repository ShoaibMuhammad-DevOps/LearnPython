a = 33
b = 200
if b > a:
  print("b is greater than a")


i=1 
while i < 6:
 print(i)
 i+=1

#break statement

i=1 
while i < 6:
 print(i)
 if i == 3:
  break
 i+=1


#continue statement

i=1 
while i < 6:
 i+=1
 if i == 3:
  continue
 print(i)
 



i=1
while i < 6:
  print(i)
  i+=1
else:
 print("I is no longer greater than 6")


#For Loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)



for x in "Banana":
 print(x)



fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break


  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
  

  