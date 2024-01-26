import pytest, module
from vector import *

class TestVec2:
  v = Vec2(1, -1)

  def test_init(self):
    assert self.v.x == 1 , "__init__(): x value"
    assert self.v.y == -1, "__init__(): y value"
  
  def test_str(self, capsys):
    print(self.v)
    captured = capsys.readouterr()
    assert captured.out == "[1, -1]\n"
  
  def test_eq(self):
    vi = Vec2(-1 , 1)
    assert (self.v == vi) == False
    assert (self.v == self.v) == True
  
  def test_add(self):
    vi = Vec2(-1, 1)
    assert ((self.v + vi) == Vec2(0, 0)) == True
  
  def test_sub(self):
    vi = Vec2(-1, 1)
    assert ((self.v - vi) == Vec2(2, -2)) == True
  
  def test_mul(self):
    assert ((self.v * 0) == Vec2(0, 0)) == True
    assert ((self.v * -1) == Vec2(-1, 1)) == True
    assert ((self.v * 2) == Vec2(2, -2)) == True
  
  def test_div(self):
    assert ((self.v / 0) == self.v) == True
    assert ((self.v / 1) == self.v) == True
    assert ((self.v / 2) == Vec2(0.5, -0.5)) == True
    assert ((self.v / -1) == self.v*-1) == True
  
  def test_dist(self):
    assert self.v.dist(Vec2(1, 1)) == 2
    assert self.v.dist(Vec2(0, -1)) == 1 
