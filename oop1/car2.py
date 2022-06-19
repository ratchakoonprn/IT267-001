class Car:
    def __init__(self,model,color,year,price) -> None:
        self.model = model
        self.color = color
        self.year = year 
        self.price = price

    #Instance Method ต้องมี self
    def print_detail(self):
        print(f"Model: {self.model}")
        print(f"Colour: {self.colour}")
        print(f"Year: {self.year}")
        print(f"Price: {self.price}")


    #Static Method ไม่ต้องมี self
    @staticmethod
    def get_static_method(text):#มี 1 argument คือ text
        print(f"String: {text}")

    #Class Method จะต้องมี cls เสมอ
    @classmethod
    def get_class_method(cls,text):
        print(f"This is class method with {text}")

if __name__ == "__main___":
    my_car = Car("Cross","White",2022,1500000)
    #call instance method
    my_car.print_detail()
    """#เรียกใช้ static method ได้ 2 แบบ
    Car.get_static_method("Hello Class")
    my_car.get_static_method("Good Car Object")
    #เรียกใช้ class method
    Car.get_class_method("Go home")"""
