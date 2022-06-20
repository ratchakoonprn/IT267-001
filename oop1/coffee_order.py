class CoffeeOrder:
    #class variables
    menu_type = "Coffee"
    total = 0
    def __init__(self,customer_name:str,menu:str,num:int=1,size:str="R") -> None:
        #instance variables
        self.customer_name = customer_name
        self.menu = menu.upper()
        self.num = num
        self.size = size.upper()
        #กำหนด price ไว้ก่อน หรือไม่ก็ได้
        self.price = 0

    def check_menu(self):
        menu_dictionary = {
            'CM':5.99,
            'CP':4.99,
            'AM':4.99,
            'CL':4.99,
            'VL':4.75,
            'ES':3.00
            }
        if self.menu in menu_dictionary:
            self.price = menu_dictionary.get(self.menu)

    def compute_price(self):
        #หาราคาต่อแก้ว
        if self.size == 'L':
            #self.price = self.price + 1
            self.price += 1
        elif self.size == 'XL':
            self.price += 1.5
        else:
            self.price

        #คำนวณราคารวม = จำนวนแก้ว * ราคา
        CoffeeOrder.total = self.num * self.price

    def display_detail(self):
        self.check_menu()
        self.compute_price()
        return f'{self.customer_name}, {self.menu} ({self.num}{self.size} * ${self.price} => ${CoffeeOrder.total}'

    def __del__(self):
        print("Object was destroyed")

if __name__ =="__main__":
    order1 = CoffeeOrder('John','es')
    order2 = CoffeeOrder('Mary','am',2,'l')

    print(order1.display_detail())
    print(order2.display_detail())