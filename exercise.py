# DON'T CHANGE Django access code START
# Our Django server is a different space than just running raw Python code.
# The code below gives us access our Django server.
# This lets us query or add data to our Django database.

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

# DON'T CHANGE Django access code END



# Write your code below

from exercises.models import *

# Function to calculate and print average
nhl = [
    { 'name': 'LA Kings', 'city': 'Los Angeles', 'attendance': [15232, 17231, 18114, 16123] },
    { 'name': 'Anaheim Ducks', 'city': 'Anaheim', 'attendance': [15232, 13231, 13114, 14634]  },
    { 'name': 'San Jose Sharks', 'city': 'San Jose', 'attendance': [19232, 17231, 18114, 19121]  },
    { 'name': 'Las Vegas Golden Knights', 'city': 'Las Vegas', 'attendance': [15232, 14231, 15114, 15512]  },
]

# first item's dictionary is LA Kings. So we print the city from that dictionary.
total = 0
games = 0
#for number in nhl[1]['attendance']:
 # if number > total:
  #  total = number

#def team_average(team_name, attendance_list):
    # Add function code here

# write for loop here

for team in nhl:
  for number in team['attendance']:
    total += number
    
  total = total/len(team['attendance'])
  print(total)
  total = 0

# for team in nhl:
#   for number in team['attendance']:
#     total += number
#   games += len(team['attendance'])
# total = total/games
# print(total)

# for team in nhl:
#   for number in team['attendance']:
#     if total < number:
#       total = number

# print(total)

# for team in nhl:
#   total = team['attendance'][0]
#   for number in team['attendance']:
#     if total > number:
#       total = number
#   print(total)
 

# for team in nhl:
#   for number in team['attendance']:
#     total += number
    
#   total = total/len(team['attendance'])
#   print(total)
#   total = 0
  #   print(total)


# age = { 'joe': 45, 'tiffany': 12, 'charlie': 62, 'helen': 32}

# print(age['tiffany'])


# list_o_lists = [ [1, 5], [2, 6, 4]]

# smallest = list_o_lists[0][0]
# # begin first for loop that loops through first level of lists
# for number_list in list_o_lists:
#     # start nested list that loops through inner list
#     for number in number_list:
#       if smallest < number:
#         smallest = number

# print(smallest)