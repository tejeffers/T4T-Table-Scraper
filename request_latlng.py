def request_latlng():
### for each restaurant, submit to google places query to return latitude and longitude
### 32200 m radius = 20 mile radius from the center of central park [@ 40.7841,-73.9661]
    T4Tout = open('T4T_restlist.txt', 'w')

    lead = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=40.7841,-73.9661&radius=32200&type=restaurant'
    with open('key.txt') as f:
        key = f.readlines()

    for item in RestNames:
        name = '&name=' + item.replace(" ", "%20")
        query = lead + name + key
        resp_json_payload = requests.get(query).json()
        if len(resp_json_payload['results']) == 0:
            print(item)
            continue
        else:
            T4Tout.write(item)
            T4Tout.write("\t")
            T4Tout.write(str(resp_json_payload['results'][0]['geometry']['location']))
            T4Tout.write("\n")

        T4Tout.close()
    return()