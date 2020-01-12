# https://wikidocs.net/28

class Cookie:
  pass

a = Cookie()
b = Cookie()

print(a)
print(b)

class FourCal:
  def __init__(self, first, second):
    self.first = first
    self.second = second
  def setdata(self, first, second):
    self.first = first
    self.second = second
  def add(self):
    return self.first + self.second
  def mul(self):
    return self.first * self.second
  def sub(self):
    return self.first - self.second
  def div(self):
    return self.first / self.second

a = FourCal(4, 3)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())

class MoreFourCal(FourCal):
  def pow(self):
    return self.first ** self.second

b = MoreFourCal(6, 3)
print(b.add())
print(b.mul())
print(b.sub())
print(b.div())
print(b.pow())

# overriding
class SafeFourCal(FourCal):
  def div(self):
    return 0 if self.second == 0 else self.first / self.second

c = SafeFourCal(4, 0)
print(c.div())

class Family:
  lastname = 'Kim'

fam1 = Family()
fam2 = Family()
print(1, fam1.lastname, id(fam1.lastname))
print(2, fam2.lastname, id(fam2.lastname))

fam1.lastname = 'Park'
print(1, fam1.lastname, id(fam1.lastname))
print(2, fam2.lastname, id(fam2.lastname))
