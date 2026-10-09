travel_log={
    "Maharashtra": ["Pune", "Mumbai", "Nashik", "Aurangabad", "Dhule", "Igatpuri"] ,
    "Tamil Nadu": ["Chennai", "Erode","Madurai"]
}
print(travel_log)
print("\n Print Mumbai from travel_log dictionary \n \n")

print(travel_log["Maharashtra"][1])

#nested lists
nested_list=["Book","Watter Bottle",["laptop","Phone", "earbuds"]]
print(nested_list)

print("\n Print earbuds from nested list: \n")
print(nested_list[2][2])


travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}

print(travel_log["Germany"]["cities_visited"][2])










# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"],
# }
#
# print(travel_log["France"][1])
#
# nested_list = ["A", "B", ["C", "D"]]
# print(nested_list[2][1])
#
# travel_log = {
#   "France": {
#     "cities_visited": ["Paris", "Lille", "Dijon"],
#     "total_visits": 12
#    },
#   "Germany": {
#     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#     "total_visits": 5
#    },
# }
#
# print(travel_log["Germany"]["cities_visited"][2])