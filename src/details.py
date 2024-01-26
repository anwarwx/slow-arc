from vector import *

'''
@brief
  represents a physical ball within the system
'''
class Ball:
  def __init__(self, a: Vec2, b: Vec2, c: Vec2):
    self.left = a
    self.center = b
    self.right = c

'''
@brief
  represents the home plate's edges within the system
'''
class HPSide:
  def __init__(self, a: Vec2, b: Vec2):
    self.front, self.back = a, b

'''
@brief
  encapsulates all relevant pitch details necessary in determining the pitch's outcome
'''
class Pitch:
  def __init__(self):
    self.path = []
    self.right_shoulder, self.left_shoulder = None, None
    self.right_knee, self.left_knee = None, None
    self.top_corner = None
    self.far_side, self.close_side = None, None
