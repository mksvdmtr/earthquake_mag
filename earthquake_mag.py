import requests
import sqlite3

# Example
#
start_time = '2018-01-01'
end_time = '2018-05-20'
latitude = '56.13'
longitude = '-106.34'
max_radius = '100'
min_magnitude = '2'

# start_time = input("Enter start time: ")
# end_time = input("Enter end time: ")
# latitude = input("Enter latitude: ")
# longitude = input("Enter longitude: ")
# max_radius = input("Enter max radius in km: ")
# min_magnitude = input("Enter min magnitude: ")


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

def write_to_db(data):
    """
    :param data: response from requests.get()
    """
    db_conn = sqlite3.connect("earthquakes.db")
    cursor = db_conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS earthquakes (number INT, place TEXT, magnitude REAL)")

    for i, d in enumerate(data['features']):

        number = i + 1
        place = d['properties']['place']
        magnitude = d['properties']['mag']
        insert = "INSERT INTO earthquakes VALUES (?, ?, ?);"
        cursor.execute(insert, (number, place, magnitude))

    db_conn.commit()
    db_conn.close()

def print_to_screen(data):
    for i, d in enumerate(data['features']):
        number = i + 1
        place = d['properties']['place']
        magnitude = d['properties']['mag']
        print(f"{number}. Place: {place}. Magnitude: {magnitude}")

#print_to_screen(data_json)
write_to_db(data_json)