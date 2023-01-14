import requests
# Api Key from weather forecast page
API_KEY = "d223a5e4db230d49bf08e031ca0a46a0"
 # modified {cityID} with {place} and {Api key} with {API_KEY} and added http://
def get_data(place, days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * days
    filtered_data = filtered_data[:nr_values]

    return filtered_data

if __name__=="__main__":
    get_data()