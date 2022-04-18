try:
  print(x)
except:
  print("An exception occurred")



try:
  print(x)
except NameError:
  print("Something else went wrong")
except:
  print("Variable x is not defined")
 
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")


try:
  f = open("demofile.txt")
  try:
    f.write("ABC")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")  