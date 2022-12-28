name1 = input("Enter you lover name :\n")
name2 = input("Enter your name :\n")

t = name1.lower().count('t')
r = name1.lower().count('r')
u = name1.lower().count('u')
e = name1.lower().count('e')

t1 = name2.lower().count('t')
r1 = name2.lower().count('r')
u1 = name2.lower().count('u')
e1 = name2.lower().count('e')

l = name1.lower().count('l')
o = name1.lower().count('o')
v = name1.lower().count('v')
e = name1.lower().count('e')

l1 = name2.lower().count('l')
o1 = name2.lower().count('o')
v1 = name2.lower().count('v')
e1 = name2.lower().count('e')

a = t+t1+r+r1+u+u1+e+e1
b = l+l1+o+o1+v+v1+e+e1

print(f"{a}{b}% ")
# Arianna Rebolini
# Channing Tatum