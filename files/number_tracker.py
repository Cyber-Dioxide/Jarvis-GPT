import datetime
import phonenumbers

import folium
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode


def location_tracker(num):
    num = num.replace(' ' , '')
    from phonenumbers import geocoder
    # num = input("Enter a number: ")
    time_ = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    API_key = "Add Your Api KEy HEre"
    sanNummber = phonenumbers.parse(num)
    location = geocoder.description_for_number(sanNummber, "en")
    sea_pro = phonenumbers.parse(num)
    servise_prover = carrier.name_for_number(sea_pro, 'en')
    geocoder = OpenCageGeocode(API_key)
    quesry = str(location)
    resltt = geocoder.geocode(quesry)
    lat = resltt[0]['geometry']['lat']
    lng = resltt[0]['geometry']['lng']
    mymap = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup=location).add_to(mymap)
    mymap.save(f"logs\\{num + str('-') + str(time_)}.html")

    return location, servise_prover, lat, lng
