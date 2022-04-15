class Human:
    #Статические поля
    default_name = 'No name'
    default_age = 0

    def __init__(self, name = default_name, age = default_age):
    #Динамические поля
        #Публичные
        self.name = name
        self.age = age

        #Приватные
        self.__money = 0
        self.__house = 'Non'

    def info(self):
    #Вывод динамического метода
        print(f'Name: {self.name}, Age: {self.age}, Money: {self.__money}, House: {self.__house}')

    #Вывод статического метода
    @staticmethod
    def default_info():
        #Обращение через Название класса.название поля
        print(f'Default_Name: {Human.default_name}, Default_Age: {Human.default_age}')

    def earn_money(self, amount):
        self.__money += amount
        print(f'Good job! Yours salary: {amount} money. Current valve: {self.__money}')

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(house, price)
        else:
            print('No enought money!')


    #Приватный метод
    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house


class House:
    def __init__(self, area, price):
        #Защищенный метод
        self._area = area
        self._price = price

    def final_price(self, discount):
        final_price = self._price * (100 - discount)/100
        print(f'Final price: {final_price}')
        return final_price

class Small_house(House):
    #Наследование класса с изменением плозади со 100 на 40
    default_area = 40

    def __init__(self, price):
        super().__init__(Small_house.default_area, price)

#Вызов методов

Human.default_info()

fedor = Human('Fedor', 32)
fedor.info()

fedor.earn_money(5000)
fedor.info()

house = House(100, 15000)
fedor.buy_house(house,3)

print('')

alexander = Human('Sasha', 25)
alexander.info()
print('')

small_house = Small_house(8500)
alexander.buy_house(small_house, 5)
print('')

alexander.earn_money(5000)
alexander.buy_house(small_house, 5)
print('')

alexander.earn_money(20000)
alexander.buy_house(small_house, 5)
alexander.info()
print('')
