class Square:
            
    def __init__(self,a):
      self.a=a
            
    def Area(self):
        Area=self.a*self.a*self.a
        return Area

    def perimeter(self):
       P=4*(self.a)
       return P