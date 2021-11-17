import math as m

# euler forward
def y0(i, h):
  if i==0:
    x, y = float(input("x(0): ")), float(input("y(0): "))
  else:
    x, y = y0(i-1, h)
  x, y = round(x,5), round(y,5)
  y1 = round(f(x,y),5)
  print(f"x{i}: {x}, y({i})= {y}, y'{i}= {y1}")
  y = y + h*y1
  x = x+h
  return x, y

# custom define derevative
def f(x, y):
  y1 = (x + m.sqrt(y))
  return y1

n = int(input("no of stages: "))
h = float(input("h: "))
y0(n, h)