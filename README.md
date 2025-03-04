### Weather API Flask Application

This project is a simple web application built with Flask that fetches weather information for a specific city using the OpenWeatherMap API. The application returns data such as temperature, weather description, humidity, and wind speed.

#### Features

- Fetches weather data for a specified city
- Returns information such as temperature, weather description, humidity, and wind speed in JSON format

#### Technologies Used

- Python
- Flask
- Requests
- Python-dotenv

#### How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/your-username/repository-name.git
cd repository-name
```

2. Create and activate a virtual environment (optional, but recommended):

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root of the project and add your OpenWeatherMap API key:

```plaintext
WEATHER_API_KEY=your_api_key_here
```

5. Run the application:

```bash
python app.py
```

The application will be running at `http://127.0.0.1:5000`.

#### How to Use

Make a GET request to the `/weather` route with the `city` parameter specifying the city you want to fetch. Example:

```bash
curl "http://127.0.0.1:5000/weather?city=Rio de Janeiro"
```

The response will be a JSON with the weather data of the specified city.

#### Example Response

```json
{
    "city": "Rio de Janeiro",
    "temperature": 25.0,
    "description": "clear sky",
    "humidity": 78,
    "wind_speed": 3.6
}
```

#### Project Structure

```plaintext
.
├── app.py
├── .env
├── requirements.txt
└── README.md
```

#### Notes

- Ensure you have an internet connection so that the application can make requests to the OpenWeatherMap API.
- Verify that your API key is correct and active.

### Contributions

Contributions are welcome! Feel free to open issues and pull requests.

---

I hope this README meets your needs. If you need any changes, let me know!
