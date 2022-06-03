import math
class Rectangle:
      def __init__(self,w,l): 
       self.w=w
       self.l = l
       A=(self.w*self.l)
       return A

      def perimeter(self):
        p=2*(self.w+self.l)
        return p              