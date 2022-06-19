class Car:
    def __init__(self,model,color,year,price) -> None:
        self.model = model
        self.color = color
        self.year = year
        self.price = price
    
    def print_detail(self):
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Year: {self.year}")
        print(f"Price: {self.price}")

if __name__ == "__main__":
    my_car = Car("Cross","White",2022,1500000)
    my_car.print_detail()