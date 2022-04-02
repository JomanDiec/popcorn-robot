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

Award.objects.all().delete()
Winner.objects.all().delete()
print(Winner.objects.all())
print(Award.objects.all())

new_awards = [
    {'name':'Best Picture',
        'winner':[{'name':'Shape of Water','year':'2018'},
        {'name':'Moonlight','year':'2017'}, {'name':'Spotlight','year':'2016'}]},
    {'name':'Stanley Cup',
        'winner':[{'name':'Washington Capitals','year':'2018'},
        {'name':'Pittsburgh Penguins','year':'2017'}]}
]

# Blog.objects.get(employee="Hurleigh Pykett").delete()

#new_salary = Employee.objects.get(employee="Heida Gill")
#new_salary.salary=78000
#new_salary.save()

#Employee.objects.all().delete()

for award in new_awards:
  new = Award.objects.create(name=award['name'])
  # new = Award.objects.get(name=award['name'])
  winner = award['winner']
  for win in winner:
    new.winner_set.create(name=win['name'], year=win['year'])
  print(new.name)
  print(new.winner_set.all())

# india = Country.objects.get(name='india')
# rica = Country.objects.get(name='costa rica')
# print(india.population)
# print(india.city_set.all())
# print(rica.population)
# print(rica.city_set.all())

print("hi, inside test!")

for i in range(3):
    print("looping 3x")