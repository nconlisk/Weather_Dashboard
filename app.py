from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv  # Required for loading .env files

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Fetch API key from environment variable
API_KEY = os.getenv("WEATHER_API_KEY")
if not API_KEY:
    raise ValueError("No API key found. Set the WEATHER_API_KEY environment variable.")

BASE_URL = "http://api.weatherapi.com/v1/current.json"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/weather", methods=["POST"])
def weather():
    location = request.form.get("location")
    if not location:
        return render_template("index.html", error="Please enter a location.")

    params = {
        "key": API_KEY,
        "q": location,
        "aqi": "yes"
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code != 200:
        return render_template("index.html", error="Failed to fetch weather data.")

    weather_data = response.json()
    return render_template("index.html", weather=weather_data)

if __name__ == "__main__":
    app.run(debug=True) 