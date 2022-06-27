class Project:
    def __init__(self,name,time,location) -> None:
        self.name = name
        self.time = time
        self._location = location
        self.__budget = 50
    
    def show(self):
        print('========== Project Detail ==========')
        print(f'name :{self.name}')
        print(f'time : {self.time} months')
        print(f'location : {self._location}')
    
    def get_budget(self):
        return self.__budget

    def update_budget(self,budget):
        self.__budget = budget