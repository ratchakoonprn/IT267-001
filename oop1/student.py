class Student:
    def __init__(self,id:str,name:str,major:str) -> None:
        self.id = id
        self.name = name
        self.major = major

    def display_detail(self):
        print(f"Id: {self.id}")
        print(f"Name: {self.name}")
        print(f"Major: {self.major}")

    def __del__(self):
        print("Object Destroyed")

if __name__ == "__main__":
    #create Jessica, John
    jessica = Student("111","Jesica","IT")
    john = Student("112","John","MKT")

    jessica.display_detail()
    john.display_detail()
