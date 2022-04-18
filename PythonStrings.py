#triple quotes string
a = """Welcome to visual code,
this lesson is for python,
In this lesson we will learn
fundamentals of python."""
print(a)


a = '''Welcome to visual code,
this lesson is for python,
In this lesson we will learn
fundamentals of python.'''
print(a)


#Slicing strings
a = "Shoaib Muhammad"
print(a[2:8])
print(a[:8])


#string functions.
print(a.lower())
print(a.upper())

#escape character.
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

#string format
txt= "The price {price: .2f} pounds"
print(txt.format(price=49.4555))

#placeholders


txt1 = "My name is {fname}, I'm {age}"
print(txt1.format(fname = "Shoaib", age = 36))
txt2 = "My name is {0}, I'm {1}".format("Shoaib",36)
print(txt2)
txt3 = "My name is {}, I'm {}".format("Shoaib",36)
print(txt3)


