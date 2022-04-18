
#search in the string
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)


#search text between range index
txt = "Hello, welcome to my world."
x = txt.index("e", 5, 10)
print(x)

txt = "Hello, welcome to my world."

print(txt.find("q"))
#print(txt.index("q"))


txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)

txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)

txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("apples")
print(x)


txt = "apple, banana, cherry"
# setting the split parameter 
x = txt.rsplit(", ")
print(x)

x = txt.rsplit(", ",1)
print(x)

