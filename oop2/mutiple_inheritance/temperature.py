class Temperature:
    def setcelcius(self,celcius:float):
        self.celcius = celcius
    
    def getcelcius(self):
        return self.celcius

    def getfahrenheit(self):
        return self.celcius * 1.8 + 32
    
    def getweather(self):
        if self.celcius <= 0:
            return 'freezing'
        elif self.celcius <= 18:
            return 'cold'
        elif self.celcius <= 28:
            return 'warm'
        else:
            return 'hot'