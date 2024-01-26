import pytest, module
from parser import *

class TestParser:
  p = Parser()
  path = "tests/input/"

  def test_file_not_found(self, capsys):
    n = self.path + "404 Not Found"
    assert self.p.parse(n) == False
    captured = capsys.readouterr()
    assert captured.out == f"file not found: {n}\n"

  def test_empty_file(self):
    n = self.path + "empty.txt"
    f = open(n, "w")
    f.close()
    assert self.p.parse(n) == False
    assert self.p.details == None
