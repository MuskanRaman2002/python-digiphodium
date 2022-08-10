def side_of_square(p=0):
    return p/4

print(side_of_square(8))

def aos(s=0):
    return s**2

print(aos(10))

p=123
side = side_of_square(p)
area = aos(side)
print(area)


p=200
area = aos(side_of_square(p))