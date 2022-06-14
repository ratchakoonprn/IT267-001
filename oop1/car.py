class Car:
    def __init__(self,model,colour,year,price) -> None:
        self.model = model
        self.colour = colour
        self.year = year
        self.price = price
    
    #instace method ต้องมี self
    def print_detail(self):
        print(f"Model: {self.model}")
        print(f"Colour: {self.colour}")
        print(f"Year: {self.year}")
        print(f"Price: {self.price}")

    def abc(self):
        print(f"Year: {self.year}")

    #static method ไม่ต้องมี self
    @staticmethod
    def get_static_method(text):#มี 1 argument คือ text
        print(f"String: {text}")

    #class method จะต้องมี cls
    @classmethod
    def get_class_method(cls,text):
        print(f"This is class method with {text}")

if __name__ == "__main__":
    my_car = Car("Cross","White",2022,1500000)
    #call instance method
    my_car.print_detail()
    #call static method
    Car.get_static_method("Hello Classs")
    my_car.get_static_method("Good Car Object")
    #call class method
    Car.get_class_method("Go home")
