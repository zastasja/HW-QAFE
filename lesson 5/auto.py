class Auto():
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def drive(self):
        print(f'{self.brand} {self.model} can drive')

    def transport(self):
        print(f'{self.brand} can deliver goods')


class Sedan(Auto):
    def __init__(self, brand, model, year, price, color):
        self.price = price
        super().__init__(brand, model, year)
        self.__color = color

    def coloration(self):
        print(f'My {self.model} is {self.__color}')

    def get_color(self):
        print(f'{self.__color} is great for the {self.model}')

    def set_color(self, newcolor):
        self.__color = newcolor


class Truck(Auto):
    def __init__(self, brand, model, year, payload):
        self.payload = payload
        super().__init__(brand, model, year)

    def load(self):
        print(f'{self.brand} can transport upto {self.payload}')


# adding sedan type car
kia = Sedan("Kia", "Rio", 2020, 3000, "red")
kia.drive()
kia.transport()
kia.coloration()
kia.set_color('blue')
kia.coloration()


# adding truck type vehicle
kassborer = Truck("Kassborer", "Tonar", 2021, "30ton")
kassborer.drive()
kassborer.transport()
kassborer.load()
