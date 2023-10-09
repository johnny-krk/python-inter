def func(a, b):
    print(a)
    print(b)
    a = 7


x = 10
y = 'a'

func(x, y)
print("x=", x)

l = [1, 2, 3, 4, 5, 6]
a = l[0]
b = l[1:]
print(a, b)
# operator rozpakowywania *
# to co rozpakuje to pakuje do listy:
al, *bl = l
print(al, bl)



