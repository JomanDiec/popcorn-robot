import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()
from exercises.models import *

credit_cards = [
    {"number":"3559711801763286","type":"jcb","name":"Eva Pinnick"},
    {"number":"5602226836687410","type":"china-unionpay","name":"Taffy Rosenwald"},
    {"number":"3545980651362518","type":"jcb","name":"Aileen Donnelly"},
    {"number":"3566179877434334","type":"jcb","name":"Cortie Venny"},
    {"number":"3581127848805810","type":"jcb","name":"Garrek Preddle"},
    {"number":"201685586642394","type":"diners-club-enroute","name":"Gaultiero Radden"},
    {"number":"675908636693920566","type":"switch","name":"Galvan Langthorne"},
    {"number":"6331104300936585936","type":"switch","name":"Brietta Lowry"},
    {"number":"3567384174874575","type":"jcb","name":"Shawna Seeler"},
    {"number":"3567301126253898","type":"jcb","name":"Jasmina Greener"}
]

for cards in credit_cards:
  Credit.objects.create(name=cards['name'], number=cards['number'], card=cards['type'])
  

print("hi, inside test!")

for i in range(3):
    print("looping 3x")