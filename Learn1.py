# привести данные в единый вид
'''
a2 = input('Введите имя: ')
a2.aqpitalize()
print ('Вы ввели - ' + a2)
'''

#Регист введо будет в формате предложения
'''
a2 = input('Введите ваше имя: ')
print('Вы ввели - ' + a2.capitalize())
'''

#Формат записи строк
'''
age3 = 27
height3 = 185
message3 = 'Вам {} лет, ваш рост {} см!' .format(age3,height3)
print(message3)
'''

#Списки
'''
a3 = [1,2,3,4,5,6,7,8,9,10]
a3[0:9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]        #первый элемент включается в список (начало с 0), а последний элемент не входит в список

>>> a3 = [1,2,3,4,5,6,7,8,9,10]
>>> a3.append(15)    #добавление списка вконце
>>> a3
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15]

>>> a4 = [1,2,3]
>>> b4 = [4,5,6]
>>> a4+b4           #сложение списков работает как и сложение строк
[1, 2, 3, 4, 5, 6]

>>> list = [1,2,3,4,5,6,7,8,9]
>>> for i in list:      #перебор всего списка
	print(i)

1
2
3
4
5
6
7
8
9

>>> com = [1,4,5,2,7,3,6,8]
>>> sorted(com)         #сортировка списка по возростанию
[1, 2, 3, 4, 5, 6, 7, 8]
'''

#Словари
'''
catalog_product = {                         #создание списка "ключ": "значение"
	"type": "phone",
	"vendor": "Apple",
	"model": "iPhone 7",
	"color": "Black",
	"price": 14.7
}
catalog_product["audio_jec"] = False        #добавить новый ключ в словарь
catalog_product['price'] = 22.5             #редактировать значение существующего ключа (поля)
print(catalog_product)
print(catalog_product['model'])             #печать Значения из Ключа

catalog_mc = catalog_product['model'] + " " + catalog_product['color']  #соединение Значений Ключей
print(catalog_mc)

catalog_vmc = catalog_product.get('vendor') + ' ' + catalog_product.get('model') + ' ' + catalog_product.get('color')
#Обращение к значениям через метод get()
print(catalog_vmc)

#Удаление ключа из словаря. Если ключа нет, тогда пропустить и не вызывать ошибку
try
    del catalog_product['owner']
except KeyError
    pass


#Заполение словаря
user_info = {
    'first_name': '',
    'last_name': ''
}
user_info['first_name'] = input('Введите ваше имя: ')
user_info['last_name'] = input('Введите вашу фамилию: ')
print('Ваше имя - ' + user_info.get('first_name'))
print('Ваша фамилия - ' + user_info.get('last_name'))
print('Ваш номер - ' + user_info.get('tel_number', 'Данные не получены'))
'''


#Пример функции
'''
def print_person(name = 'Nemo', age = 18):
    print(f'Name: {name} Age: {age}')

print_person()
print_person('Bob')
print_person('Tomy', 25)
'''


#Пример использования функции
'''
def sum (a,b): return a + b
def subtract (a,b): return a - b
def multiply (a,b): return a * b
def division (a,b): return a // b

def select_operation (choice):
    if choice == 1:
        return sum              #  return lambda a, b: a + b  можно использовать инструкцию на одну строчку
    elif choice == 2:
        return subtract
    elif choice == 3:
        return multiply
    elif choice:
        return division
    else:
        return

operation = select_operation(1)
print (operation(10,5))

operation = select_operation(2)
print (operation(10,5))

operation = select_operation(3)
print (operation(10,5))

operation = select_operation(4)
print (operation(10,5))
'''


# Создание классов
'''
class Person:

    def __init__(self, name):       # Инкапсуляция (скрытие, инициализация, приватный тип) метода
        self.name = 'No name'
        self.__age = 1              # Устанавливаем возраст
        self.city = 'No registration'
        self.h = 1
        self.w = 1

    @property                       # Геттер, который берет значение с параметра после проверки
    def age (self):
        return self.__age

    @age.setter                     # Сеттер проверяет вводымые данные и меняет значение параметра
    def age (self, age):
        if 1 < age < 110:
            self.__age = age
        else:
            print('Недопустимый возраст')

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, City: {self.city}, Height: {self.h}cm., Weight: {self.w}kg..")

tom = Person ('Tom')
tom.name = 'Tom'
tom.age = 27
tom.city = 'New York'
tom.w = 50
tom.display_info()

bob = Person ('Bob')
bob.name = 'Bob'
bob.age = 221
bob.display_info()

'''

# Работа с датой и временем
'''
import locale
from datetime import datetime, timedelta
locale.setlocale(locale.LC_TIME, 'ru_RU')
d_n = datetime.now()
print('Date_Time now: ' + str(d_n))
dt_now_form = d_n.strftime('%-d.%-m.%Y %H:%m')
print('Date_Time now in form: ' + dt_now_form)

dt2 = datetime(2022, 4, 1, 0, 0, 0)
print('Date_Time dt2: ' + str(dt2))
dt2_f = dt2.strftime('%A %d %B %Y')
print('dt2 in format: ' + dt2_f)

delta = d_n - dt2
print('Delta date_time: ' + str(delta))
'''


#Создание Телеграм бота
'''
from telegram.ext import Updater, CommandHandler

def start_bot(bot, update):
    mytext = """Привет пользователь!   #Для ввода текста в несколько строк

Я простой бот, который умеет искать информацию.

Для начала давайте начнем /start
	"""
    print(update)
    update.message.reply_text(mytext)


def main():
    updtr = Updater("5268755750:AAEcSi0bFuN3DHk1B_euHUQDMfCZSzrgsnc")

    updtr.dispatcher.add_handler(CommandHandler("start", start_bot))
    updtr.start_polling()
    updtr.idle()


if __name__ == "__main__":
    main()
'''
