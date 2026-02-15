from django.shortcuts import render
import requests

API_KEY = "6988e872adc6da16b008b21b4748b8ea"

def home(request):
    context = {}

    if request.method == "POST":
        city = request.POST.get('city')

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            context = {
                "city": city,
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "description": data["weather"][0]["description"],
            }
        else:
            context = {
                "error": "City not found"
            }

    return render(request, "core/home.html", context)