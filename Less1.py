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

'''
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