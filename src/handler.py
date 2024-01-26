from parser import *
from details import *

# global constants
P_WIDTH = 21.59  # PLATE WIDTH
B_WIDTH = 9.652  # BALL WIDTH

'''
@brief
  Responsible for determining if a pitch is a ball or strike
'''
class OutcomeHandler:
  '''
  @brief
    default constructor
  '''
  def __init__(self):
    self.strike_zone = False
    self.home_plate = False
    self.outcome = "BALL"

  '''
  @brief
    lets us know when the ball is close to the batter
  @param
    y: y-coord of the ball
    y_min: y-coord of the batter's left shoulder
    y_max: y-coord of the batter's left knee
  @return
    true if the y-coord is within the min and max bound
  '''
  def close(self, y, y_min, y_max):
    return y >= y_min and y <= y_max

  '''
  @brief
    lets us know if the ball is within the strike-zone
  @param
    x: x-coord of ball
    y: y-coord of ball
    x_min: x-coord of either the batter's left shoulder or left knee
    y_min: y-coord of the batter's left shoulder
    y_max: y-coord of the batter's left knee
  @return
    true if the x, y coords are within the polygon
  '''
  def inside(self, x, y, x_min, x_max, y_min, y_max):
    return x >= x_min and x <= x_max and y >= y_min and y <= y_max

  '''
  @brief
    lets us if the ball is above the home plate
  @param
    p: width of the ball
    z_min: width of far side of home plate
    z_max: width of close side of home plate
  @return
    true if the ball is within the home plate
  '''
  def between(self, p, z_min, z_max):
    return p >= z_min and p <= z_max

  '''
  @brief
    transforms the strike zone on top of the home plate if needed
  @param
    details: Pitch object containing pitch details
  '''
  def transform_strike_zone(self, details: Pitch):
    diff = (details.left_knee.x - details.close_side.front.x)
    if (diff > P_WIDTH or (diff*-1) > P_WIDTH):
      details.left_knee -= Vec2(diff, 0)
      details.right_knee -= Vec2(diff, 0)
      details.left_shoulder -= Vec2(diff, 0)
      details.right_shoulder -= Vec2(diff, 0)

  '''
  @brief
    determines whether the pitch is a ball or strike
  @param
    details: Pitch object containing the pitch details 
  @return
    true if able to determine pitch outcome
  '''
  def determine_call(self, details: Pitch) -> bool:
    self.outcome = "BALL"
    self.strike_zone, self.home_plate = False, False

    if details is None: return False

    self.transform_strike_zone(details)

    f_width = details.far_side.front.dist(details.far_side.back)
    c_width = details.close_side.front.dist(details.close_side.back)

    i, size = 0, len(details.path)
    for i in range(i, size):
      if (not self.close(details.path[i].center.y, details.left_shoulder.y, details.left_knee.y)):
        continue
      if (not ((size - i+1) % 2)):
        break

    j = i+1
    while (i < size and j < size):
      pos = details.path[i].center
      des = details.path[j].center
      while (not pos.dist(des) < 1):
        dir = (des - pos).unit()
        pos += dir

        x_min = details.left_knee.x
        if details.left_shoulder.x < details.left_knee.x:
          x_min = details.left_shoulder.x

        x_max = details.right_knee.x
        if details.right_shoulder.x > details.right_knee.x:
          x_max = details.right_shoulder.x
        
        if (self.inside(pos.x, pos.y, x_min, x_max, details.left_shoulder.y, details.left_knee.y)):
          self.strike_zone = True

      b_width = details.path[i].left.dist(details.path[i].right)
      if (self.between(b_width/B_WIDTH, f_width/P_WIDTH, c_width/P_WIDTH)):
        self.home_plate = True

      i+=1; j+=1

    if self.strike_zone and self.home_plate:
      self.outcome = "STRIKE"

    return True
