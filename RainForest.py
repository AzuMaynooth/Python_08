import datetime
import requests
import json
import os
from geopy.geocoders import Nominatim


# Get tomorrow's date
def get_next_day():
    return (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")

#  Get rainfall information from Open-Meteo API
def get_weather_status(latitude, longitude, date):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=precipitation_sum&timezone=auto&start_date={date}&end_date={date}"

    #print("API URL:", url)
    response = requests.get(url)
    #print("API Response:", response.text)  # Debugging line
    if response.status_code == 200:
        weather_data = response.json()
        #print("Weather Data:", weather_data)  # Debugging line
        if weather_data.get("daily") and weather_data["daily"].get("precipitation_sum"):
            precipitation = weather_data["daily"]["precipitation_sum"][0]
            return precipitation
    return None

# Read info
def read_results(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    return {}

# Safe results
def save_results(file_path, results):
    with open(file_path, "w") as file:
        json.dump(results, file)

# Get city coordinates
def get_coordinates(city_name):
    geolocator = Nominatim(user_agent="weather_app")
    location = geolocator.geocode(city_name)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

# Results file
results_file = "weather_results.json"

# Read previous results
results = read_results(results_file)

# Ask to the user city name and date
while True:
    city_name = input("Enter the city name: "
                      "\nIf you want to end the program write end")
    latitude, longitude = get_coordinates(city_name)

    if city_name.lower() == 'end':
        break  # Exit the loop if the user enters 'end'

    if latitude is None or longitude is None:
        print(f"Could not find coordinates for {city_name}. Please try again.\n")

    # Ask user date
    while True:
        time_str = input("Add date (YYYY-MM-DD) \n"
                         "or\n"
                         "press enter to get tomorrow's information: ")
        if not time_str:
            time_str = get_next_day()
            break
        try:
            datetime.datetime.strptime(time_str, "%Y-%m-%d")
            break
        except ValueError:
            print("Incorrect date format, please try it again.")

    # Verify if info is saved
    if time_str in results:
        precipitation = results[time_str]
    else:
        # Get meteorological information
        precipitation = get_weather_status(latitude, longitude, time_str)
        results[time_str] = precipitation
        save_results(results_file, results)

    # Display results
    if precipitation is None:
        print(f"No data available for {city_name} on {time_str}\n")
    elif precipitation > 0.0:
        print(f"Rainfall for  {city_name} on {time_str} \n {precipitation} mm.")
    else:
        print(f"No rain for {city_name} on {time_str}\n")
