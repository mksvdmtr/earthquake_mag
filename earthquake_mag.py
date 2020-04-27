import requests

# Example
#
# start_time = '2018-01-01'
# end_time = '2018-05-20'
# latitude = '56.13'
# longitude = '-106.34'
# max_radius = '100'
# min_magnitude = '2'

start_time = input("Enter start time: ")
end_time = input("Enter end time: ")
latitude = input("Enter latitude: ")
longitude = input("Enter longitude: ")
max_radius = input("Enter max radius in km: ")
min_magnitude = input("Enter min magnitude: ")


url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'

data = requests.get(url, headers={'Accept': 'application/json'},
                    params={
                        'format':'geojson',
                        'starttime':start_time,
                        'endtime':end_time,
                        'latitude':latitude,
                        'longitude':longitude,
                        'maxradius':max_radius,
                        'minmagnitude':min_magnitude
                    })

data_json = data.json()

for i, d in enumerate(data_json['features']):
    print(f"{i + 1}. Place: {d['properties']['place']}. Magnitude: {d['properties']['mag']}")

