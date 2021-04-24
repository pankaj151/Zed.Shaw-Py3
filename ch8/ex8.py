formatter = "{} {} {} {}" #it's  a variable formatter user defined
print(formatter.format(1,2,3,4)) # it,s calling format() func and printing out the values.
print(formatter.format("one","two","Three","Four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter,formatter,formatter,formatter))
print(formatter.format(
"Try your",
"own test here",
"Maybe a poem",
"or a song about fear"
))

