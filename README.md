# Python_08

In this exercise, you will write a program that checks if it's going to rain on a particular day using the provided weather API. The program will ask the user for a date in the "YYYY-mm-dd" format, for example, "2023-11-03". If no date is provided, the application should consider the next day as the date to check the weather. The program will then make a request to the API to fetch the weather status.

1. Ask the user for a date in "YYYY-mm-dd" format to check the weather.
2. If no date is provided, consider the next day as the date to check the weather.
3. Make a request to the API to fetch the weather status for the given date.
4. The possible precipitation states are:
  - "It will rain" for a result greater than 0.0. Print the precipitation value for the user (for example 
  - "It will not rain" for a result equal to 0.0
  - "I don't know" when there is no result or the result is negative
5. Save the query results to a file. If the date is already present in the file, do not make a request to the API, instead, return the result from the file.

API Documentation:
https://open-meteo.com/en/docs 

API Endpoint URL: `https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=precipitation_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}`

Replace the parameters: `latitude`, `longitude`, and `searched_date` in the URL.

Hints:

- Use Python's `datetime` module to manipulate dates.
- Use the `requests` library to make API requests.
- Use Google Maps or OpenStreetMap to get the latitude and longitude values for the city you want to check
- Remember to handle exceptions that may occur during the API request.
- Use Python's file handling methods to read and write to a file.
- Validate the user input to ensure it's in the correct format.

Additional Challenge (Optional):

Enhance your program to handle multiple locations. The user can input the latitude and longitude for the location they want to check the weather for. You can use the “geocoder” library for getting the latitude and longitude based on user input. 

Geocoder documentation: https://geocoder.readthedocs.io/
