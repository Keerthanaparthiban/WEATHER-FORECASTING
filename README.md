# DAILY WEATHER FORECASTING USING MACHINE LEARNING [![](https://camo.githubusercontent.com/2fb0723ef80f8d87a51218680e209c66f213edf8/68747470733a2f2f666f7274686562616467652e636f6d2f696d616765732f6261646765732f6d6164652d776974682d707974686f6e2e737667)](https://python.org)


# Weather Forecasting Using Python

Weather forecasting is the application of science and technology to predict the conditions of the atmosphere for a given location and time. Weather forecasts are made by collecting as much data as possible about the current state of the atmosphere (particularly the temperature, humidity and wind) and using understanding of atmospheric processes (through meteorology) to determine how the atmosphere evolves in the future. 

This project is used to demonstrate the working of a Weather App in Python using Tkinter module. This GUI app will tell us the current weather of a particular city along with temperature details along with other details. The data's have been fetched from Open weather map which helps us to access current weather data for any location on Earth including over 200,000 cities! 

# Open Weather Map and Postman API

OpenWeatherMap is an online service, owned by OpenWeather Ltd, that provides global weather data via API, including current weather data, forecasts, nowcasts and historical weather data for any geographical location. The company provides a minute-by-minute hyperlocal precipitation forecast for any location.

Firstly, we have to use a weather API to fetch the data from the Open Weather Map website by generating an API key.

Steps to Generate an API Key : 

1.) Login in to Open Weather Map https://openweathermap.org/

2.) Go to the API section. Then in the Current Weather Data section click on the Api doc.

3.) Now in the API Call section, we have the link of api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
Click on the API key on the link it will direct to the page from where you can get the key.

The generated key looks like this:

![image](https://user-images.githubusercontent.com/92458543/139553551-db02ee8c-9d83-422b-b0f9-98fc5a9a38c5.png)

After generating an API key, we use Postman which is an application used for API testing. An HTTP client that tests HTTP requests, utilizing a graphical user interface, through which we obtain different types of responses that need to be subsequently validated. 

-> Login in to Postman https://www.postman.com/

-> Go to workspace section and paste the API call link . eg : api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key} in the URL request bar and click send.

![image](https://user-images.githubusercontent.com/92458543/139554328-015e3027-bd60-4f53-9d56-9bee3af6b215.png)

-> Copy paste the API key in {API key} and enter a city in name eg: bangalore in {city name} of API call link.

![image](https://user-images.githubusercontent.com/92458543/139554825-0b5f7887-2cfc-4dc6-bcb6-e5f1a6f79762.png)

-> We get a JSON file which contains the coordinates, weather informations like wind speed, humidity, temperature, pressure and etc. Refer to the JSON file available above for more info.

![image](https://user-images.githubusercontent.com/92458543/139554878-f2aaa1be-df10-4672-a857-33d15283a631.png)

-> Copy paste the URL eg: api.openweathermap.org/data/2.5/weather?q=bengaluru&appid=ecfcab314f94f193575dc2f93927fcd7 in the browser to get a proper link of the JSON files.

![image](https://user-images.githubusercontent.com/92458543/139555112-c404785d-ab7f-49c1-be77-251693ba71d8.png)

# Steps to create Python Script

1.) Import the modules 

Modules used :

Tkinter: It is a built-in python library for making GUI using tkinter toolkit.

Requests: It is a library which helps in fetching the data with the help of URL.

2.) Create the body of the GUI with the help of tkinter.

3.) Load the key and URL in the program by cpoy pasting it in an variable eg: api. To set the city name we can replace the default city given in the link with a city variable which will help us access an city.

4.) Make a getweather() function to get the weather of a particular location.

5.) Search function so that we can get the output weather details.

# OUTPUT 

Now, we can access the current weather details of any city in the world. 

In the below snapshot you can see the current weather details like Temperature, Pressure, Humidity, Sunrise and Sunset time of the city Delhi in India.

![image](https://user-images.githubusercontent.com/92458543/139555610-a56ef71b-7e69-4987-987e-567a26995910.png) 

## Connect with me! 🌐
Known on internet as ** Keerthana Parthiban **

[<img target="_blank" src="https://img.icons8.com/bubbles/100/000000/linkedin.png" title="LinkedIn">](https://www.linkedin.com/in/keerthana-p-aa1725205)   [<img target="_blank" src="https://img.icons8.com/bubbles/100/000000/github.png" title="Github">](https://github.com/Keerthanaparthiban)

## Email Me :e-mail:

[<img target="_blank" src="https://img.icons8.com/bubbles/100/000000/secured-letter.png" title="Mail me">](mailto:keerthanap2435@gmail.com)
