class House():
  def ___init___(self): 
    self.NumberOfResidents 
    self.NumberOfResidentsMax
    self.QualityOfHousing

  def upgrade(self):
    self.level += 1
    self.NumberOfResidentsMax =  self.NumberOfResidentsMax * self.level
    print("Это здание теперь вмещает", self.NumberOfResidentsMax ,"Жильцов!")

class PrivateHouse(House):
    self.NumberOfResidents = 0
    self.NumberOfResidentsMax = 5 * self.level
    self.QualityOfHousing = 0.67


class BarackHouse(House):
    self.NumberOfResidents = 0
    self.NumberOfResidentsMax = 20 * self.level
    self.QualityOfHousing = 0.67


class ApartmentHouse(House):
    self.NumberOfResidents = 0
    self.NumberOfResidentsMax = 50 * self.level
    self.QualityOfHousing = 0.89


class MansionHouse(House):
    self.NumberOfResidents = 0
    self.NumberOfResidentsMax = 5 * self.level
    self.QualityOfHousing = 0.99
