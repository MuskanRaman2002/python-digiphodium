from turtle import *

def pentagon(size=50):
    fillcolor('red')
    begin_fill()
    for i in range(5):
        forward(size)
        left(72) 

def triangle(size=50):
   for i in range(3):
     forward(size)
     left(120)

for i in range(6):
    if i % 2==0:
        pentagon(100)
    else:
            triangle(100)
    left(60)

mainloop()