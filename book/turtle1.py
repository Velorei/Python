Python 3.11.2 (v3.11.2:878ead1ac1, Feb  7 2023, 10:02:41) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
t = turtle.Pen()
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.reset()
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
SyntaxError: multiple statements found while compiling a single statement
t.clear()
t.backward(100)
t.up()
t.right(90)
t.forward(20)
t.left(90)
t.down()
t.forward(100)

t.reset()
t.forward(100)
t.left(90)
t.forward(20)
t.left(90)
t.forward(100)
t.left(90)
t.forward(20)
t.left(90)
t.up()
t.right(90)
t.forward(50)
t.down()
t.left(90)
t.forward(200)
t.left(135)
t.forward(200)
t.left(135)
t.rigth(45)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    t.rigth(45)
AttributeError: 'Turtle' object has no attribute 'rigth'. Did you mean: 'right'?
t.right(45)
t.forward(200)
t.left(135)
t.forward(100)
t.up()
t.left(90)
t.right(180)
>>> t.forward(100)
>>> t.right(90)
>>> t.down()
>>> t.right(180)
>>> t.forward(200)
>>> t.up()
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t.down()
>>> t.forward(200)
>>> t.up()
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t.down()
>>> t.forward(200)
>>> t.up()
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t.down()
>>> d.forward(200)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    d.forward(200)
NameError: name 'd' is not defined. Did you mean: 'id'?
>>> t.forward(200)