from datetime import datetime

class Person:
  def __init__(self, name, country, dob):
    self.name = name
    self.country = country

    # date is entered in yyyy-mm-dd string format
    self.dob = datetime.strptime(dob, "%Y-%m-%d")

  def calculate_age(self):
    today = datetime.today()
    return round(((today - self.dob).days / 365.25))
  

james = Person("James", "US", "2004-10-10")
james_age = james.calculate_age()
print(james_age)
