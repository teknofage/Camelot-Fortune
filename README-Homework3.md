# Fortune Form

Fortune Form is an app for questing knights who want to meet new people

## Installation

Install Python, Flask, brew

## Usage

```python
import 

By entering multiple values as answers to the questions in the form, Fortune Form can deliver your personal fortune based on your personal details and answers.

HOMEWORK 3 DISCUSSION QUESTIONS

1. Describe the data contained in the API response. What can we discern about the weather in the specified city?

The data consists of a lot of small dictionaries containing key value pairs in the form of JSON data. We can discern from this data about San Francisco: the latitude and longitude, the description of the weather today (scattered clouds), the temperature, pressure, humidity, as well as information about the wind and sunrise and sunset times, and th time zone data.

2. How would we obtain the temperature in the specified city? Describe using Python dictionary syntax. (HINT: Assume that the JSON response is stored in a variable called json_response.)

I wil use the requests.get function to send a GET request to the API. 

import requests
response=requests.get(response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=San+Francisco&appid=2608f679d4594364525f6c6cc2246c79", params=parameters)
)