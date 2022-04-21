import requests


def get_wether(url):
    result = requests.get(url)
    if result.status_code == 200:
        # result.json()['name'] выводит значения
        return result.json()
    else:
        print("Соединение нарушено!")


if __name__ == "__main__":
    data = get_wether(
        "https://api.openweathermap.org/data/2.5/weather?q=Kharkiv&units=metric&lang=ru&APPID=da287acf40fccbf5f017dfbe6561ed20")
    print(data)
