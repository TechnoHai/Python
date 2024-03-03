travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


# 🚨 Do NOT change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇


# noinspection PyDictCreation
def add_new_country(input_country, input_visits, input_cities):


    new_country = {}

    new_country["country"] = input_country
    new_country["visits"] = input_visits
    new_country["cities"] = input_cities
    travel_log.append(new_country)


# new_country_russia = {
#     "country": "Russia",
#     "visits": 2,
#     "cities": ["Moscow", "Saint Petersburg"]
# }
add_new_country("israel", 5, ["ashkelon", "tel-aviv"])
# travel_log.append(new_country_russia)
# 🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
