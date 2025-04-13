# Calculator class for basic arithmetic operations

class Calculator:
  def __init__(self):
    pass

  def add(self, a, b):
    return a + b
  
  def sub(self, a, b):
    return a - b
  
  def mult(self, a, b):
    return a * b
  
  def div(self, a, b):
    return a / b
  
casio = Calculator()

num1, num2 = 5, 10

op_add = casio.add(num1, num2)
op_sub = casio.sub(num1, num2)
op_mult = casio.mult(num1, num2)
op_div = casio.div(num2, num1)

print(op_add)
print(op_sub)
print(op_mult)
print(op_div)
