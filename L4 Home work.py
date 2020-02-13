import turtle
import time
a=turtle.Turtle()
b=input("螺旋邊數")
a.shape('turtle')
for c in range(1,41,3):
    for d in range(int(b)):
        time.sleep(0.01)
        a.forward(0.1*c)
        a.right(180/int(b))
        