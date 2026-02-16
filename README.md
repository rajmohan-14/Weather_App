🌦️ Weather Dashboard

A web-based Weather Dashboard built using Django that allows users to search for real-time weather information of any city. The application fetches live weather data from a weather API and displays temperature, humidity, wind speed, and weather conditions in a clean UI.

🚀 Features

🔍 Search weather by city name

🌡️ Display temperature (°C / °F)

💧 Humidity information

🌬️ Wind speed details

🌤️ Weather condition with icons

📱 Responsive design

🗂️ Simple and clean UI

🛠️ Tech Stack

Backend: Django (Python)

Frontend: HTML, CSS, Bootstrap

Database: SQLite (default Django DB)

API: OpenWeatherMap API (or any weather API used)

📂 Project Structure
weather-dashboard/
│
├── manage.py
├── db.sqlite3
├── config/          # Project settings
│
├── weather/         # Main weather app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   └── static/
│
└── README.md
⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/weather-dashboard.git
cd weather-dashboard
2️⃣ Create Virtual Environment
python -m venv venv

Activate it:

Mac/Linux

source venv/bin/activate

Windows

venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt

If requirements.txt is not created, install manually:

pip install django requests
4️⃣ Add Weather API Key

In views.py, replace:

api_key = "YOUR_API_KEY"

Get your API key from:
👉 https://openweathermap.org/api

5️⃣ Run Migrations
python manage.py migrate
6️⃣ Start the Server
python manage.py runserver

Open in browser:

http://127.0.0.1:8000/
📸 Screenshots

(Add your project screenshots here once deployed)

📈 Future Improvements

🌍 5-day weather forecast

📍 Detect user location automatically

🌙 Dark mode

📊 Weather history tracking

🐳 Docker deployment

🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

📄 License

This project is open-source and available under the MIT License.
