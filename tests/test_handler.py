import pytest, module
from handler import *
from parser import *

PATH = "tests/input/"

class TestHandler:
  h = OutcomeHandler()
  p = Parser()

  def test_close(self):
    assert self.h.close(0, 0, 0) == True
    assert self.h.close(-1, -1, 1) == True
    assert self.h.close(1, 0, 5) == True
    assert self.h.close(-1, 0, 5) == False

  def test_transform_behind(self):
    if (self.p.parse(PATH + "behind.txt")):
      if (self.h.determine_call(self.p.details)):
        assert self.h.outcome == "STRIKE"
  
  def test_transform_infront(self):
    if (self.p.parse(PATH + "infront.txt")):
      if (self.h.determine_call(self.p.details)):
        self.h.outcome == "STRIKE"
