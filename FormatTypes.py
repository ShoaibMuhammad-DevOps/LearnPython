#Use "<" to left-align the value:

txt = "We have {:>8} chickens."
print(txt.format(49))

txt = "The temperature is between {:-} and {:+} degrees celsius."
print(txt.format(-3, 7))

txt = "The universe is {:,} years old."

print(txt.format(13800000000))


txt = "You scored {:%}"
print(txt.format(0.25))

#Or, without any decimals:

txt = "You scored {:.0%}"
print(txt.format(0.025))
