class Animal:
    #class varaible
    animal = "CAT"

    def new_animal(self,name:str,breed:str,colour:str,age:int):
        #instance variable
        self.name = name
        self.breed = breed
        self.colour = colour
        self.age = age


    def print_detail(self):
        print(f"***********")
        print(f"Name: {self.name}")
        print(f"Animal: {self.animal}")
        print(f"Breed: {self.breed}")
        print(f"Colour: {self.colour}")
        print(f"Age: {self.age}")

#create object
if __name__ == "__main__":
    Animal.animal = "FISH"
    ula = Animal()  
    ula.new_animal("Ula","Scottish","White",1)
    ula.animal = "DOG"
    ula.print_detail()

    drac = Animal()
    drac.new_animal("Drac","Scottish","White",1)
    drac.print_detail()
    drac.breed = "Catfish"
    drac.print_detail()

    #เรียกดูข้อมูลของ object ผ่านทางชื่อ Class
    Animal.print_detail(ula) #ula.print_detail()
    Animal.print_detail(drac) # drac.print_detail()

    #เรียกดู class varibale ทั้งหมด
    print(f'{Animal.__dict__}')

    #เรียกดู instance varibale ทั้งหมด
    print(f'{ula.__dict__}')