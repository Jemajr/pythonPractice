# class to represent a shape
class Shape:
  def perimeter(self):
    pass

  def area(self):
    pass


class rectangle(Shape):
  def __init__(self, length, width):
    self.length = length
    self.width = width

  def perimeter(self):
    return 2 * (self.length + self.width)

  def area(self):
    return self.length * self.width
  

class triangle(Shape):
  def __init__(self, base, height, side1, side2, side3):
    self.base = base
    self.height = height
    self.side1 = side1
    self.side2 = side2
    self.side3 = side3

  def perimeter(self):
    return self.side1 + self.side2 + self.side3
  
  def area(self):
    return 0.5 * self.base * self.height
  

box = rectangle(5, 10)
box_p = box.perimeter()
box_a = box.area()

print("Box perimeter:", box_p)
print("Box area:", box_a)