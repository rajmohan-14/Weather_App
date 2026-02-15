from django.shortcuts import render
import requests

API_KEY = "6988e872adc6da16b008b21b4748b8ea"

def home(request):
    context = {}

    if request.method == "POST":
        city = request.POST.get('city')

        url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200 and "list" in data:

            current = data["list"][0]

            daily_forecast = []
            for item in data["list"]:
                if "12:00:00" in item["dt_txt"]:
                    daily_forecast.append({
                        "date": item["dt_txt"].split(" ")[0],
                        "temp": item["main"]["temp"],
                        "icon": item["weather"][0]["icon"],
                    })

            context = {
                "city": city,
                "temperature": current["main"]["temp"],
                "description": current["weather"][0]["description"],
                "icon": current["weather"][0]["icon"],
                "forecast": daily_forecast[:5]
            }

        else:
            context["error"] = "City not found"

    return render(request, "core/home.html", context)