import requests
# Api Key from weather forecast page
API_KEY = "d223a5e4db230d49bf08e031ca0a46a0"
 # modified {cityID} with {place} and {Api key} with {API_KEY} and added http://
def get_data(place, days = None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered = data["list"]
    nr_values = 8 * days
    filtered = filtered[:nr_values]
    if kind == "Temperature":
        filtered = [dict["main"]["temp"] for dict in filtered ]
    elif kind == "Sky":
        filtered = [dict["weather"][0]["main"] for dict in filtered]
    return filtered

if __name__=="__main__":
    get_data(place = "Tokyo", days =3, kind = "Temperature")