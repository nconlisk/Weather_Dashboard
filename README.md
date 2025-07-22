# Weather Dashboard 🌦️

A lightweight Flask web application that fetches and displays real-time weather data for any location using the [WeatherAPI](https://www.weatherapi.com/). Designed for developers learning Flask, API integrations, or pytest.

---

## Technologies Used
- **Backend**: Python + Flask  
- **Frontend**: HTML/CSS (vanilla, no JavaScript)  
- **API**: [WeatherAPI](https://www.weatherapi.com/)  
- **Testing**: pytest + requests-mock  
- **Deployment**: Heroku-ready (with `gunicorn`)  

---

## Dependencies
### Core
```text
flask==2.3.2
python-dotenv==1.0.0
requests==2.31.0
```

### Testing
```text
pytest==7.4.0
pytest-cov==4.1.0
requests-mock==1.11.0
```

Install all:  
```bash
pip install -r requirements.txt
```

---

## Key Features
- Fetch current weather (temperature, conditions)  
- Error handling for invalid inputs/API failures  
- Minimalist UI  

---

## Quick Start
1. **Clone and setup**:
   ```bash
   git clone https://github.com/your-username/Weather_Dashboard.git
   cd Weather_Dashboard
   echo "WEATHER_API_KEY=your_key_here" > .env
   pip install -r requirements.txt
   ```

2. **Run**:
   ```bash
   python app.py
   ```
   Visit `http://localhost:5000`.

---

## Testing
```bash
# Run tests
pytest -v

# With coverage
pytest --cov=.
```

---

## Deployment (Heroku)
1. Add `gunicorn` to `requirements.txt`  
2. Create `Procfile`:
   ```procfile
   web: gunicorn app:app
   ```
3. Deploy:
   ```bash
   heroku create
   git push heroku main
   ```

---

## How to Contribute
1. Fork the repo  
2. Create a branch (`git checkout -b feature/your-idea`)  
3. Commit changes (`git commit -m "Add feature"`)  
4. Push (`git push origin feature/your-idea`)  
5. Open a PR  

---

## License
MIT