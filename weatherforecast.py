import datetime
import tkinter as tk
from pip._vendor import requests
import time

def getWeather(canvas):
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=ecfcab314f94f193575dc2f93927fcd7"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    e = datetime.datetime.now()
    datee = e.strftime("%d/%m/%Y")
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 21600))

    final_date = "DATE: " + datee 
    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Max Temp: " + str(max_temp) + "°C" + "\n" + "Min temp: " + str(min_temp) + "°C" + "\n" + "Pressure: " + str(pressure) + " Pa" + "\n" + "Humidity: " + str(humidity) + " %" + "\n" + "Wind Speed: " + str(wind)  + " kmph" + "\n" + "Sunrise: " + sunrise  + " AM" + "\n" + "Sunset: " + sunset  + " PM"
    label1.config(text = final_date)
    label2.config(text = final_info)
    label3.config(text = final_data)
    

canvas = tk.Tk()
canvas.geometry("500x500")
canvas.title("Daily Weather Forecasting")

d=("poppins", 15, "bold")
f=("poppins", 15, "bold")
t=("poppins", 30, "bold")

textfield = tk.Entry(canvas, font = t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font = d)
label1.pack()
label2 = tk.Label(canvas, font = t)
label2.pack()
label3 = tk.Label(canvas, font = f)
label3.pack()

canvas.mainloop()