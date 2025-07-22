# Weather_Dashboard
A Simple Weather Dashboard created with Cursor and DeepSeek V3.1 to test coding capabilities.

Explanations and usage detailed below:
## Key Code Snippets
### Flask App (`app.py`)
```python
from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
API_KEY = os.getenv("WEATHER_API_KEY")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/weather", methods=["POST"])
def weather():
    location = request.form.get("location")
    if not location:
        return render_template("index.html", error="Please enter a location.")
    
    params = {"key": API_KEY, "q": location, "aqi": "yes"}
    response = requests.get("http://api.weatherapi.com/v1/current.json", params=params)
    if response.status_code != 200:
        return render_template("index.html", error="Failed to fetch weather data.")
    
    return render_template("index.html", weather=response.json())
```

### HTML Template (`templates/index.html`)
```html
<!DOCTYPE html>
<html>
<head>
    <title>Weather Dashboard</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <h1>Weather Dashboard</h1>
    <form method="POST" action="/weather">
        <input type="text" name="location" placeholder="Enter location">
        <button type="submit">Get Weather</button>
    </form>
    {% if error %}
        <p class="error">{{ error }}</p>
    {% endif %}
    {% if weather %}
        <div class="weather-data">
            <h2>{{ weather.location.name }}</h2>
            <p>Temperature: {{ weather.current.temp_c }}°C</p>
            <p>Condition: {{ weather.current.condition.text }}</p>
        </div>
    {% endif %}
</body>
</html>
```

## Testing
Run tests (functional + unit tests):
```bash
pytest -v
```
**Test Coverage**:
```bash
pytest --cov=.
```

## API Reference
- **Endpoint**: `POST /weather`
  - **Request**: `location` (string, required)
  - **Response**: Weather data (JSON) or error message.

## Deployment
### Heroku (Example)
1. Install Heroku CLI and login.
2. Create a `Procfile`:
   ```procfile
   web: gunicorn app:app
   ```
3. Deploy:
   ```bash
   heroku create
   git push heroku main
   ```

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

## License
MIT