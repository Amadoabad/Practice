import requests
import json
from datetime import datetime
# Getting latitude & longitude for certain city
def get_lat_lon(city):
    '''
    Calling openweathermap to get the Lattiude and Longitude needed for the OneCallapi
    Input : city : The city name you want to get the Lattitude and Longitude for
    Output : Returns the Latitude 'lat' and Longitude 'lon'
    '''
    key = "a2cc4594865cb6c214d64dbf42b0aea5" # api key
    base_url = "http://api.openweathermap.org/data/2.5/weather?&units=metric&" # Base Url for the api
    complete_url = base_url+"q="+city+"&appid="+key # Creating the complete url
    response = requests.get(complete_url) # calling the api for a response
    info = response.json() # The Complete info the response holds
    lat = info['coord']['lat']
    lon = info['coord']['lon']
    return lat, lon
# Getting the forcast 
def get_forcast(lat, lon):
    '''
    Function return forcast for weather
    Input: 
            lat & lon: Lattitude and Longitude of the place you want to get forcast for
    Output:
            Returns a dictionary of weather for current time and 7 days in advance
    '''
    key = "a2cc4594865cb6c214d64dbf42b0aea5" # api key
    base_url = "https://api.openweathermap.org/data/2.5/onecall?&units=metric" # Base Url for the api
    complete_url = f"{base_url}&lat={lat}&lon={lon}&exclude=minutely,hourly&appid={key}"  # Creating the complete url
    response = requests.get(complete_url) # calling the api for a response
    info =response.json() # The Complete info the response holds
    current = info['current']# The section 'current' in the response
    temp = int(current['temp']) # The current temperature
    dict_of_weather = {'current': temp}
    for i in range(8):
        date = datetime.fromtimestamp(info['daily'][i]['dt']).date()
        temp = info['daily'][i]['temp']
        dict_of_weather[str(date)] = temp
    return dict_of_weather

# Getting the exact temprature needed 
def get_temp(dict_of_weather, date = None, time = None):
    '''
    Function to get a specific temperature
    Input: 
        dict_of_weather: Dictionary of keys: dates as string and the first key is 'current' for the current time
                                       values: dictionary for temperature and the first value is a scalar value
        date : Default value of 'current' for the current moment or else enter a date yyyy-MM-dd 
                if entered wrong value will work as 'current'
        time : Default value of 'day' can take other values like ('min', 'max', 'night', 'eve', 'morn')
        '''
    if date in dict_of_weather.keys():
        if time in ['day', 'min', 'max', 'night', 'eve', 'morn']:
            
            temp = dict_of_weather[date][time]
        else:
            temp = dict_of_weather[date]['day']
    else:
        temp = dict_of_weather['current']
    return round(temp)
# Recommending clothes according to temperature 
def recommend(temp, city):
    '''
    Function to recommend colthes according to the temperature
    Input : temp : the temperature as integer
    Output : returns a string with a recommendation 
    '''
    wearings_dict = {
        tuple(range(-10, 0)) : "a",
        tuple(range(0, 10)) : "b",
        tuple(range(10, 20)) : "c",
        tuple(range(20, 30)) : "d"
    } # Add or edit temperatures and their interpretation
    # For loop to print the right interpretation of the temperature 
    for key, value in wearings_dict.items():
        if temp in key:
            return f"temperature is around {temp} in {city} , You better wear {value}"
# Calling the Functions
city = 'LinköPing'
lat, lon = get_lat_lon(city)
dict_of_weather = get_forcast(lat, lon)
temp = get_temp(dict_of_weather)
print(f"It's around {temp} in {city} now")
input()
##recommendation = recommend(temp, city)
##print(recommendation)
