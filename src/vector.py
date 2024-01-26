import math

EPS = 0.0000001

'''
@brief
  a 2D vector class for x, y coordinate computation
'''
class Vec2:
  def __init__(self, x, y):
    self.x, self.y = x, y
  
  def __str__(self):
    return f"[{self.x}, {self.y}]"
  
  def __eq__(self, v):
    return self.dist(v) < EPS
  
  def __add__(self, v):
    return Vec2(self.x + v.x, self.y + v.y)
  
  def __mul__(self, s):
    return Vec2(self.x * s, self.y * s)

  def __sub__(self, v):
    return self + (v*-1)
  
  def __truediv__(self, s):
    if (s == 0): return self
    return self * (1/s)
  
  def __abs__(self):
    return math.sqrt(self.x**2 + self.y**2)

  def dist(self, v):
    return abs(self - v)
  
  def unit(self):
    if (abs(self) < EPS): return self
    return self / abs(self)
