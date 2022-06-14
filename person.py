class Person:
    def __init__(self,name,gender,profession,hours) -> None:
        self.name = name
        self.gender = gender
        self.profession = profession
        self.hours = hours

    def work(self):
        print(f"{self.name} is working as a {self.profession}")

    def study(self):
        print(f"{self.name} studies for {self.hours} hour(s)")
    
    def show(self):
        print(f"Name: {self.name} Gender: {self.gender} Profession: {self.profession} Study: {self.hours}")

#create object
jessa = Person("Jessa","Male","Software Engineer",10)
jessa.show()
jessa.work()
jessa.study()

jon = Person("Jon","Male","Doctor",15)
jon.show()
jon.work()
jon.study()

lalisa = Person("Lalisa","Female","Korean Singer",13)
lalisa.work()