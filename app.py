from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "35cb9b8e16f1077eb60b7b38d464754c"

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None

    if request.method == "POST":
        city = request.form["city"]

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        data = requests.get(url).json()

        if data.get("cod") != "404":
            weather_data = {
                "city": city.upper(),
                "temp": round(data["main"]["temp"]),
                "feels": round(data["main"]["feels_like"]),
                "humidity": data["main"]["humidity"],
                "weather": data["weather"][0]["description"],
                "wind": data["wind"]["speed"]
            }
        else:
            weather_data = {"error": "City not found"}

    return render_template("index.html", weather=weather_data)


if __name__ == "__main__":
    # 🔥 IMPORTANT CHANGE (phone lo work avvadaniki)
    app.run(host="0.0.0.0", port=5000, debug=True)
    