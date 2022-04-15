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
