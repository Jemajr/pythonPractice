
class Circle:
  def __init__(self, radius):
    self.radius = radius

  def get_perimeter(self):
    return round((2 * 3.14 * self.radius), 2)
  
  def get_area(self):
    return round((3.14 * (self.radius)**2), 2)
  

first_circle = Circle(10)
first_circle_perimeter = first_circle.get_perimeter()
first_circle_area = first_circle.get_area()

print(first_circle_perimeter)
print(first_circle_area)
