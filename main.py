from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])


def get_weather():
    if request.method == "POST":
        city = request.form["city"]
    else:
        city = "Waterloo"

    construct_url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + "f520801048ecbd469c711ad583c1be23"

    response = requests.get(construct_url)
    list_of_data = response.json()
    print(list_of_data)

    data = {
        "country_code": str(list_of_data['sys']['country']),
        "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
        "temp_cel": str(round(list_of_data['main']['temp'] - 273.15)) + 'C',
        "pressure": str(list_of_data['main']['pressure']) + "hPa",
        "humidity": str(list_of_data['main']['humidity']) + "%",
        "wind_speed": str(round(list_of_data["wind"]["speed"] * 3.6)) + "km/h",
        "cityname": city
    }
    return render_template('weather.html',data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
