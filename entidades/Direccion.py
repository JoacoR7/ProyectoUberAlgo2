
class Direccion:
    ex = None
    ey = None
    dx = None
    dy = None

    def __init__(self, ex, ey, dx, dy):
            self.ex = ex
            self.ey = ey
            self.dx = dx
            self.dy = dy

    def getEx(self):
          return self.ex
    
    def getEy(self):
          return self.ey
    
    def getDx(self):
          return self.dx
    
    def getDy(self):
          return self.dy
    
    def setEx(self,ex):
          self.ex = ex

    def setEy(self,ey):
          self.ey = ey

    def setDx(self,dx):
          self.dx = dx

    def setDy(self,dy):
          self.dy = dy

          