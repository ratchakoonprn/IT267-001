class Area:
    def __init__(self,base=1,high=1) -> None:
        self.__base = base
        self.__high = high
     
    #getter base, high
    @property
    def base(self):
        return self.__base
    @property
    def high(self):
        return self.__high

    #setter base,high
    @base.setter
    def base(self,value):
        self.__base = value

    @high.setter
    def high(self,value):
        self.__high = value
    
    #common method
    def compute_area(self):
        return (0.5 * self.base * self.high)

    