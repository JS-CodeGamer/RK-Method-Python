import math as m

# modified euler:
def y0(i, h):
  if i>0:
    x, y = y0(i-1, h)
  if i==0:
    x, y = float(input("x(0): ")), float(input("y(0): "))
  y1 = round(f(x,y),5)
  y1_half = round(f(x+(h/2), y+(h/2)*y1),5)
  print(f"x{i}: {x}, y({i})= {y}, y'{i}= {y1}, y'({i}+1/2)={y1_half}")
  y = y + h*y1_half
  x = x+h
  x, y = round(x,5), round(y,5)
  return x, y

# custom define derevative
def f(x, y):
  y1 = (x + m.sqrt(y))
  return y1

n = int(input("no of stages: "))
h = float(input("h: "))
y0(n, h)