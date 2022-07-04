from shape import Shape
from math import pi

class Square(Shape):
    def __init__(self, length = 0) -> None:
        super().__init__("Square")
        self.__length = length
    
    @property
    def length(self):
        return self.__length
    @length.setter
    def length(self,value):
        self.__length = value
    
    #overriding
    def computer_area(self):
        super().computer_area()
        self.area = self.length ** 2
        #area มาจาก superclass Animal
    
    #new method
    def print_square(self):
        self.computer_area()
        print(f'{self.shape} area = {self.area:,.2f}')
        #shape มาจาก superclass Animal

class Circle(Shape):
    def __init__(self, radius = 0) -> None:
        super().__init__("Circle")
        self.__radius = radius
    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self,value):
        self.__radius = value
    
    def computer_area(self):
        super().computer_area()
        self.area = pi * (self.radius ** 2)
    
    def print_circle(self):
        self.computer_area()
        print(f'{self.shape} area = {self.area:,.2f}')

class Triangle(Shape):
    def __init__(self, base = 0, high = 0) -> None:
        super().__init__("Triangle")
        self.__base = base
        self.__high = high
    
    @property
    def base(self):
        return self.__base
    @base.setter
    def base(self,value):
        self.__base = value
    
    @property
    def high(self):
        return self.__high
    @high.setter
    def high(self,value):
        self.__high = value
    
    def computer_area(self):
        super().computer_area()
        self.area = 0.5 * self.base * self.high
    
    def print_triangle(self):
        self.computer_area()
        print(f'{self.shape} area = {self.area:,.2f}')