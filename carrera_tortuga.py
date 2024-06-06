from turtle import *
from random import randint
speed(0)
penup()
goto(-140, 140)

for paso in range(15):
  write(paso, align='center')
  right(90)

  for _ in range(15):  
    pendown()
    forward(5)  
    penup()
    forward(5)  

  forward(10)  
  penup()
  backward(160)
  left(90)
  forward(20)

# Crea las tortugas
enner = Turtle()
enner.color('red')
enner.shape('turtle')
enner.penup()
enner.goto(-160, 120)

tony = Turtle()
tony.color('blue')
tony.shape('turtle')
tony.penup()
tony.goto(-160, 90)

juan = Turtle()
juan.color('green')
juan.shape('turtle')
juan.penup()
juan.goto(-160, 60)

moises = Turtle()
moises.color('yellow')
moises.shape('turtle')
moises.penup()
moises.goto(-160, 30)

victor = Turtle()
victor.color('black')
victor.shape('turtle')
victor.penup()
victor.goto(-160, 0)

for turn in range (1000) :
       
        enner.forward(randint(1,5))
        tony.forward(randint(1,5))
        juan.forward(randint(1,5))
        moises.forward(randint(1,5))
        victor.forward(randint(1,5))

     
for giro in range (8) :
      enner.right(randint(1,5))
      tony.right(randint(1,5))
      juan.right(randint(1,5))
      moises.right(randint(1,5))
      victor.right(randint(1,5))