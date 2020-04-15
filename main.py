import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from test_prog import Ui_Dialog
import requests
import json

app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

def get_city(city_name_input):
    try:
        adress = 'https://geocode-maps.yandex.ru/1.x/?format=json&apikey=fa43b26e-20a6-4297-aa30-2320569ee59d&geocode=' + city_name_input
        c = requests.get(adress)
        data = c.json()
        coordinates_line = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        city_name = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']['Components'][-1]
        coordinates = coordinates_line.split()
        city_name = city_name['name']
        lon = coordinates[0]
        lat = coordinates[1]
        return city_name, lon, lat
    except:
        pass

def get_weather(lon, lat):
    try:
        w = requests.get('https://api.weather.yandex.ru/v1/informers?lat=' + lat + '&lon=' + lon,
        headers = {'X-Yandex-API-Key':'02e7aaae-d1a5-4339-bb2a-f802ec822f8d'})
        w_data = w.json()
        temp = w_data["fact"]["temp"]
        feels_like = w_data["fact"]["feels_like"]
        condition = w_data["fact"]["condition"]
        humidity = w_data["fact"]["humidity"]
        pressure_mm = w_data["fact"]["pressure_mm"]
        wind_speed = w_data["fact"]["wind_speed"]
        return temp, feels_like, condition, humidity, pressure_mm, wind_speed
    except:
        pass

def choose_clothes(temp, condition):
    temp = int(temp)
    result = "none"
    condition_beautiful = "none"
    if condition == "clear" or condition == "partly-cloudy" or condition == "overcast":
        condition_beautiful = "fine"
    else:
        condition_beautiful = "bad"
    temp_beautiful = "none"
    if temp >= 10:
        temp_beautiful = "hot"
    else:
        temp_beautiful = "cold"
    if condition_beautiful == "fine" and temp_beautiful == "hot":
        result = "Today is clear and not cold. Wear any clothing."
    elif condition_beautiful == "fine" and temp_beautiful == "cold":
        result = "It's cold today, but clear. Dress warmly."
    elif condition_beautiful == "bad" and temp_beautiful == "hot":
        result = "Today it is warm, but may rain. Put on a raincoat"
    elif condition_beautiful == "bad" and temp_beautiful == "cold":
        result = "It may rain today, and very cold. Dress very warmly."
    else:
        result = "I'm broken. My programmer is very bad."
    return result

def complete_all():
    city_name_input = ui.lineEdit_2.text()
    try:
        city_name, lon, lat = get_city(city_name_input)
        temp, feels_like, condition, humidity, pressure_mm, wind_speed = get_weather(lon, lat)
        prediction = choose_clothes(temp, condition)
        ui.lineEdit_3.setText(city_name)
        temp = str(temp)
        feels_like = str(feels_like)
        humidity = str(humidity)
        pressure_mm = str(pressure_mm)
        wind_speed = str(wind_speed)
        ui.label_7.setText(temp + "°C")
        ui.label_11.setText(feels_like + "°C")
        ui.label_8.setText(wind_speed + "m/s")
        ui.label_9.setText(humidity + "%")
        ui.label_10.setText(pressure_mm + "mm Hg")
        ui.label_16.setText(prediction)
    except:
        # ui.label_14.setText('City entered incorrectly, try again')
        ui.label_7.setText('')
        ui.label_11.setText('')
        ui.label_8.setText('')
        ui.label_9.setText('')
        ui.label_10.setText('')
        ui.label_16.setText('')
        ui.lineEdit_3.setText("Error! City entered incorrectly")

ui.pushButton.clicked.connect(complete_all)

sys.exit(app.exec_())
