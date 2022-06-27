class Vehicle:
    def __init__(self,name,wheels,max_speed,vin) -> None:
        #public attribute
        self.name = name
        self.wheels = wheels
        #protected attribute
        self._max_speed = max_speed
        #private attribute
        self.__vin = vin

    def set_vin(self,vin):
        self.__vin = vin

    def v_detail(self):
        print('==================')
        print(f'name : {self.name}')
        print('==================')
        print(f'wheels : {self.wheels}')
        print(f'max_speed : {self._max_speed}')
        print(f'vin : {self.__vin}')