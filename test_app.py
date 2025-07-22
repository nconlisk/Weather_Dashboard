import pytest
from app import app
import os

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """Test the home page route returns successfully"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Weather Dashboard" in response.data  # Assuming this is in your index.html

def test_weather_route_success(client, monkeypatch):
    """Test successful weather data retrieval"""
    # Mock the API response
    mock_response = {
        'location': {'name': 'London'},
        'current': {'temp_c': 15, 'condition': {'text': 'Cloudy'}}
    }
    
    def mock_get(*args, **kwargs):
        class MockResponse:
            def json(self):
                return mock_response
            status_code = 200
        return MockResponse()
    
    monkeypatch.setattr('requests.get', mock_get)
    
    response = client.post('/weather', data={'location': 'London'})
    assert response.status_code == 200
    assert b"London" in response.data
    assert b"15" in response.data
    assert b"Cloudy" in response.data

def test_weather_route_missing_location(client):
    """Test error when location is missing"""
    response = client.post('/weather', data={'location': ''})
    assert response.status_code == 200
    assert b"Please enter a location" in response.data

def test_weather_route_api_failure(client, monkeypatch):
    """Test error when API request fails"""
    def mock_get(*args, **kwargs):
        class MockResponse:
            def json(self):
                return {}
            status_code = 400
        return MockResponse()
    
    monkeypatch.setattr('requests.get', mock_get)
    
    response = client.post('/weather', data={'location': 'London'})
    assert response.status_code == 200
    assert b"Failed to fetch weather data" in response.data

def test_missing_api_key(monkeypatch):
    """Test error when API key is missing"""
    monkeypatch.delenv('WEATHER_API_KEY', raising=False)
    with pytest.raises(ValueError, match="No API key found"):
        from app import app  # This will trigger the API key check 