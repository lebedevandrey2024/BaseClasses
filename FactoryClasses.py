class Factory():
  def ___init___(.self):

    self.Squares = [] #список занимемых квадратов. в СвЕТОВЫХ КОДАХ [[001, 001, 001],[002, 001, 001]] смотри доску в https://miro.com/app/board/uXjVLNKZfEk=/
    self.Area = self.Pos_x 
    
    self.Effective
    
    self.TypeOfResourceExport
    
    self.Level #от 1 до 10
    
    self.StockCapacityExport
    self.StockCapacityMaxExport
    #Импорт добавляем понадобномти
    
    self.EfficiencyLossRate
    
    self.EfficiencyLossCounter
    
  def EfficiencyLoss(): #потеря эффективность когда счетчик EfficiencyLossCounter заполняеться!
    self.EfficiencyLossCounter += 1
    if self.EfficiencyLossCounter >= self.EfficiencyLossRate:
      self.Effective -= 0.01

  def ProductionProcess():
    self.TypeOfResourceExport += 1 * self.EfficiencyLossCounter * self.level


class FarmFactory(Factory):
  def ___init___(.self):
    self.SoilQuality
    
    self.StockCapacityMaxExport = 24 * self.level
    self.EfficiencyLossRate = 10 # недель это для теста
    self.TypeOfResourceExport = "Урожай"
#########################################################
class IronMineFactory(Factory):
  def ___init___(.self):
    self.MiningOfResource
    
    self.StockCapacityMaxExport = 50 * self.level
    self.EfficiencyLossRate = 10 # недель это для теста
    self.TypeOfResourceExport = "Железная Руда"

class CoalMineFactory(Factory):
  def ___init___(.self):
    self.MiningOfResource
    
    self.StockCapacityMaxExport = 50 * self.level
    self.EfficiencyLossRate = 10 # недель это для теста
    self.TypeOfResourceExport = "Угольная Руда"
#########################################################
class FoodFactory(Factory):
  def ___init___(.self):
    self.StockCapacityMaxExport = 24 * self.level
    self.EfficiencyLossRate = 10 # недель это для теста
    self.TypeOfResourceImport = "Урожай"
    self.TypeOfResourceExport = "Пища"

  def ProductionProcess():
    if self.TypeOfResourceImport >= 1 * self.EfficiencyLossCounter * self.level:
      self.TypeOfResourceImport -= 1 * self.EfficiencyLossCounter * self.level
      self.TypeOfResourceExport += 1 * self.EfficiencyLossCounter * self.level
    
class BeerFactory(Factory):
  def ___init___(.self):
    self.StockCapacityMaxExport = 24 * self.level
    self.EfficiencyLossRate = 10 # недель это для теста
    self.TypeOfResourceImport = "Урожай"
    self.TypeOfResourceExport = "Пиво"


  def ProductionProcess():
    if self.TypeOfResourceImport >= 1 * self.EfficiencyLossCounter * self.level:
      self.TypeOfResourceImport -= 1 * self.EfficiencyLossCounter * self.level
      self.TypeOfResourceExport += 1 * self.EfficiencyLossCounter * self.level
    
class MeatFactory(Factory):
  def ___init___(.self):
    self.StockCapacityMaxExport = 24 * self.level
    self.EfficiencyLossRate = 10 # недель это для теста
    self.TypeOfResourceImport = "Урожай"
    self.TypeOfResourceExport = "Mясо"


  def ProductionProcess():
    if self.TypeOfResourceImport >= 1 * self.EfficiencyLossCounter * self.level:
      self.TypeOfResourceImport -= 1 * self.EfficiencyLossCounter * self.level
      self.TypeOfResourceExport += 1 * self.EfficiencyLossCounter * self.level
    
#########################################################







