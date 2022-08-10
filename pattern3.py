from turtle import *

for i in range(6):
    print(i, i%3)
    if i % 3 == 0:
        color('red')
    elif i % 3 == 1:
        color('cyan')
    else:
        color('purple')
    forward(100)
    left(360/6)
mainloop()