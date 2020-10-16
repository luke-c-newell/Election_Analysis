# counties = ["Arapahoe","Denver","Jefferson"]
# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not in the list of counties.")
# for county in counties:
#     print(county)
# for num in range(5):
#     print(num)

# counties_dict = {
#     "Arapahoe": 422829, 
#     "Denver": 463353, 
#     "Jefferson": 432438
#     }

# # for county in counties_dict.keys():
# #     print(county)
# # for voters in counties_dict.values():
# #     print(voters)
# # for county, voters in counties_dict.items():
# #     print(county, "county has", voters, "registered voters.")

# voting_data =  [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]

# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)
# for county_dict in voting_data:
#     print(county_dict['county'])

# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")

# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# print(f"I received {my_votes / total_votes * 100}% of the total votes.")

# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters} registered voters.")

# for county, voters in counties_dict.items()
# print(f"{county} county has {voters:,.} registered voters")

# counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters:,} registered voters.")

# for county_dict in voting_data:
#     for county, voters in county_dict.items():
#         print(f"'{county}' county has '{voters:,}'' registered voters.")

# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)