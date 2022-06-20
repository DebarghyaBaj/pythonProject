a = "my NaMe is Khan"

print(a.capitalize())
# This will be capitalized the first character of the string.

print(a.casefold())
# Convert string into lowercase.

print(a.center(30, "!"))
# put the string some padding.

print(a.count('a'))
# Print the occurrence of 'a'.

txt = "My name is Ståle"
print(txt.encode(encoding="ascii", errors="backslashreplace"))
print(txt.encode(encoding="ascii", errors="ignore"))
print(txt.encode(encoding="ascii", errors="namereplace"))
print(txt.encode(encoding="ascii", errors="replace"))
print(txt.encode(encoding="ascii", errors="xmlcharrefreplace"))
# encode the string.

print(a.endswith('n'))
# true if it ends with 'n'.

txt1 = "H\tE\tE\tL\tL\tO"
print(txt1)
# print with 1 tab as mentioned
print(txt1.expandtabs(2))
# print with 4 tabs
