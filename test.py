# import requests
# from pprint import pprint
#
# LAT = "-20.523140"
# LON = "-43.696660"
#
#
# params = {
#     "lat": LAT,
#     "lon": LON,
#     "radius": 500,
#     "location_types": "airport"
# }
#
# header = {
#     "apikey": "pKwf1zfMH1WKvJX2h_jSd0kJLw3RQ4eN"
# }
# response = requests.get(url="https://tequila-api.kiwi.com/locations/radius", params=params, headers=header)
# response.raise_for_status()
# pprint(response.json())

# import requests
# # import os
#
# SHEETY_ENDPOINT = "https://api.sheety.co/4d2c366e5ea28ffd64068039bffdd6d9/flightTravel/users"
#
#
# def get_email():
#     users_first_write_email = input("\nWhat's your email? ")
#     users_second_write_email = input("\nPlease rewrite your email: ")
#
#     if users_first_write_email == users_second_write_email:
#         print("\nCongratulations, you're in !")
#         return users_first_write_email
#     else:
#         print("\nSomething is diferent, please write again")
#         get_email()
#
#
# users_first_name = str(input("\nWhat's your first name? "))
# users_Last_name = input("\nWhat's your last name? ")
# users_email = get_email()
#
# sheety_users_params = {
#     "user": {
#         "firstName": users_first_name,
#         "lastName": users_Last_name,
#         "email": users_email,
#     }
# }
#
# response = requests.post(url=SHEETY_ENDPOINT, json=sheety_users_params)
# response.raise_for_status()
#
# print(response.json())
# import codecs
# place = "São paulo"
# SOME = codecs.encode(obj=place, encoding="ascii")
# codecs.replace_errors(SOME)
