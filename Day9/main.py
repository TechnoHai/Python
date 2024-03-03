# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
#     "Loop": "An action of doing the same thing over and over again",
# }
# # print(programming_dictionary["Bug"])
# # print(programming_dictionary)
# #
# # #adding new key to a dictionary
# # programming_dictionary["hai"] = "learning python my dude"
# # print(programming_dictionary)
# #
# # #create an empty dictionary
# # empty_dictionary = {}
#
# # clear a dictionary from its DATA
# # programming_dictionary = {}
#
# # change the value of a key in dictionary
# # print(programming_dictionary["Bug"])
# # programming_dictionary["Bug"] = "we just overwrite Bug Value "
# # print(programming_dictionary["Bug"])
#
# # Look through a dictionary
#
# #Nesting
# capitals = {
#   "France": "Paris",
#   "Germany": "Berlin",
# }
#
# #Nesting a List in a Dictionary
#
# # travel_log = {
# #   "France": ["Paris", "Lille", "Dijon"],
# #   "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# # }
#
# #Nesting Dictionary in a Dictionary
# # travel_log = {
# #   "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 5 },
# #   "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 12},
# # }
#
# #Nesting Dictionary in a list
# travel_log = [
#     {
#      "country": "France",
#      "cities_visited": ["Paris", "Lille", "Dijon"],
#      "total_visits": 5
#      },
#
#     {
#      "country": "Germany",
#      "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#      "total_visits": 12
#      },
# ]
#
#
# print(travel_log[0])
order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}
print(order["main"][2])
