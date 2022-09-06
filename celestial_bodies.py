import ephem
import datetime


def calculate_sun_distance():
    """Calculates distance between planet and the sun on a given date. Planet defaults to Jupiter,
    date defaults to current date"""
    query = input("Select planet: ").title() or "Jupiter"
    date = input("Enter a date yyyy/mm/dd, default is today: ") or datetime.date.today().strftime("%Y/%m/%d")
    try:
        celestial_body = getattr(ephem, query)()
        celestial_body.compute('2022/1/1')
        distance_au_units = celestial_body.sun_distance
        distance_km = distance_au_units * 149597870.691

        print(f"{query} is {distance_au_units} from the sun on the {date}")
        print(f"{distance_au_units} AU = {distance_km} km")
    except AttributeError:
        print(f"Couldn't find {query}, please try again")


calculate_sun_distance()
