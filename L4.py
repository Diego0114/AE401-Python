import turtle
import time
a=turtle.Turtle()
b=turtle.Turtle()
a.shape('turtle')
b.shape('turtle')
a.color('purple')
b.color('red')
for c in range(36000):
    time.sleep(0.001)
    a.forward(0.01)
    a.right(0.01)
for c in range(3600):
    time.sleep(0.01)
    b.forward(0.1)
    b.right(0.1)
turtle.done()
