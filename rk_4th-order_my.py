# Python program to implement Runge Kutta 4th order method
import math as m

# custom define derevative
def f(x, y):
  y1 = (-y)
  return y1

# Finds value of y for a given x using step size h
# and initial value y0 at x0.
def y0(i, h):
  if i>0:
    x, y = y0(i-1, h)
  if i==0:
    x, y = float(input("x(0): ")), float(input("y(0): "))
  k1 = h*f(x, y)
  k2 = h*f(x+(h/2), y+(k1/2))
  k3 = h*f(x+(h/2), y+(k2/2))
  k4 = h*f(x+h, y+k3)
  k1, k2, k3, k4 = map(lambda x: round(x, 5), (k1, k2, k3, k4))
  print(f"i={i:>2}, xi: {x:>10}, yi= {y:>10}, k1= {k1:>10}, k2= {k2:>10}, k3= {k3:>10}, k4= {k4:>10}")
  y = y + (1/6)*(k1 + (2*k2) + (2*k3) + k4)
  x, y = round(x+h,5), round(y,5)
  return x, y

# Driver method
n = int(input("no of stages: "))
h = float(input("h: "))
y0(n, h)