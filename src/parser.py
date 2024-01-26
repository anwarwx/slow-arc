import csv
from vector import *
from details import *

'''
@brief
  Responsible for parsing pitch data file into a Pitch object
'''
class Parser:
  '''
  @brief
    default constructor
  '''
  def __init__(self):
    self.data = None
    self.details = None

  '''
  @brief
    parses a given pitch data file into a Pitch object
  @param
    file_name: name of the file containing pitch details
  @return
    true if able to parse file contents
  '''
  def parse(self, file_name: str) -> bool:
    self.data = []
    try:
      with open(file_name, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
          data = []
          for val in row:
            data.append((int)(val))
          self.data.append(data)
    except OSError as e:
      print(f"file not found: {file_name}")
      return False
    
    if len(self.data) < 10:
      return False

    self.details = Pitch()
    self.details.right_shoulder = Vec2(self.data[5][0], self.data[5][1])
    self.details.left_shoulder = Vec2(self.data[6][0], self.data[6][1])
    self.details.right_knee = Vec2(self.data[7][0], self.data[7][1])
    self.details.left_knee = Vec2(self.data[8][0], self.data[8][1])
    self.top_corner = Vec2(self.data[2][0], self.data[2][1])
    self.details.close_side = HPSide(
      Vec2(self.data[0][0], self.data[0][1]),
      Vec2(self.data[1][0], self.data[1][1]))

    self.details.far_side = HPSide(
      Vec2(self.data[4][0], self.data[4][1]),
      Vec2(self.data[3][0], self.data[3][1]))

    size = len(self.data)
    for i in range(9, size):
      self.details.path.append(Ball(
        Vec2(self.data[i][3], self.data[i][4]),
        Vec2(self.data[i][1], self.data[i][2]),
        Vec2(self.data[i][5], self.data[i][6])))
    
    return True
