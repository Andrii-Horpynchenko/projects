from datetime import datetime
from flask import Flask, request
from Req import get_wether
from News_list import all_news

#Переменные для запроса
city = "Kharkiv"
metric = "metric"
lang = "ru"
api_key = "da287acf40fccbf5f017dfbe6561ed20"

app = Flask(__name__)


@app.route("/")
def message_main():  # Обращение к запросу через УРЛ
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units={}&lang={}&APPID={}" .format(
        city, metric, lang, api_key)
    weather = get_wether(url)
    cut_date = datetime.now().strftime("%-d.%-m.%Y %H:%m")
    result = "<p>Погода в городе: </p><h3>{}</h3>" .format(weather['name'])
    result += "<p>Дата:</p> <h3>{}</h3>" .format(cut_date)
    result += "<p>Температура:</p> <h3>{}</h3>" .format(
        weather['main']['temp'])
    result += "<p>Чувствуется как:</p> <h3>{}</h3>" .format(
        weather['main']['feels_like'])
#     result += "<p>Облачность: </p><h3>{}</h3>" .format(weather['weather']['description'])
    result += "<p>Скорость ветра: </p><h3>{}</h3>" .format(
            weather['wind']['speed'])  # Обращение к параметру
    return result
    # Нужно возвращать значеня через return, а не print!


@app.route("/meteo")
def get_meteo():
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units={}&lang={}&APPID={}" .format(
        city, metric, lang, api_key)
    meteo_data = get_wether(url)
    return str(meteo_data)


@app.route("/news-<int:news_id>")
def news_page(news_id):
    news_show = [news for news in all_news if news['id'] == news_id]
    if len(news_show) == 1:
        result = "<h1>%(title)s</h1><p><i>%(date)s</i></p><p>%(text)s</p>"
        result = result % news_show[0]
        return result


@app.route("/filters")
def filters_all():
    limit_list = range(0, 100, 1)
    # Числа от 0 до -9 с шагом -1: range(0, -10, -1))
    limit = int(request.args.get('limit')) if int(
            request.args.get('limit')) in limit_list else 50
#Перебор числовых значений переменной limit в списке limit_list от 0 до 100 с шагом 1 и дефолтным значением 50
    color_list = ["green", "blue", "red"]
    color = request.args.get('color') if request.args.get(
        'color') in color_list else 'black'
    result = '<h1 style = "color: %s">Filter parametrs: <small>%s</small></h1>' % (
        color, limit)
    return result


if __name__ == "__main__":
    app.run(port=5020, debug=True)
