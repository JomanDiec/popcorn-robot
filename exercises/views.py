# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Superhero, Animal, Car, Stock, Credit, Blog, Phone
from django.urls import reverse
from exercises.models import *
from django.db.models.functions import Lower
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User

# Create your views here.
def superheroes(request):

    # code below!
    superheroes = Superhero.objects.filter(is_male=False).filter(
        is_male=False).filter(name__contains="e").order_by("name")[:5]

    context = {'superheroes': superheroes}
    return render(request, 'exercises/superhero.html', context)


def animals(request):
    animals = None

    # code below!
    animals = Animal.objects.filter(birthplace__contains="Brazil")

    context = {'animals': animals}
    return render(request, 'exercises/animal.html', context)


def cars(request):
    cars = None

    # code below!
    cars = Car.objects.filter(
        make__contains="toyota").order_by("-model").filter(year__gte=1995)

    context = {'cars': cars}
    return render(request, 'exercises/car.html', context)


def templates(request):

    superheroes = Superhero.objects.filter(is_male=False).filter(rating__gte=7)
    animals = Animal.objects.filter(birthplace="china").filter(
        name__startswith="g").order_by("-name")
    cars = Car.objects.filter(year__gte=2010)

    context = {'superheroes': superheroes, 'animals': animals, 'cars': cars}
    return render(request, 'exercises/template.html', context)


def summary(request):

    employees = Employee.objects.order_by("-salary")[:5]

    context = {'employees': employees}
    return render(request, 'exercises/summary.html', context)


def submit_form(request):
    context = {}
    return render(request, "exercises/submit_form.html", context)


def team_edward(request):
    return HttpResponse(request.POST['message'] +
                        " is a fervent supporter of team edward")


def team_jacob(request):
    return HttpResponse(request.GET['first_name'] + " " +
                        request.GET["last_name"] +
                        " is a member of team jacob. ROAR!!")


def bert(request):
    context = {}
    return render(request, "exercises/bert.html", context)


def ernie(request):
    return HttpResponse(request.POST['body_text'])


def create_page(request):
    return HttpResponse("hello you")


def forrest_gump(request):
    return HttpResponse("life is like a box of chocolates")


def wizard_of_oz(request):
    context = {}
    return render(request, 'exercises/wizard_of_oz.html', context)


def the_godfather(request):
    return HttpResponse("I'm gonna make him an offer he can't refuse.")


def casablanca(request):
    context = {}
    return render(request, 'exercises/casablanca.html', context)


def stocks(request):
    stocks = Stock.objects.order_by('-market_cap')[:5]

    context = {'stocks': stocks}
    return render(request, 'exercises/stocks.html', context)


def credit(request):
    credit = Credit.objects.order_by('id')

    context = {'credit': credit}
    return render(request, 'exercises/credit.html', context)


def credit_details(request, credit_details_id):

    credit = Credit.objects.get(id=credit_details_id)

    context = {'credit': credit}
    return render(request, 'exercises/credit_card_details.html', context)


def new_page(request):
    context = {}
    return render(request, 'exercises/new_page.html', context)


def blog(request):
    blog = Blog.objects.all()

    context = {'blog': blog}
    return render(request, 'exercises/blog.html', context)


def blog_post(request, blog_post_id):

    blog = Blog.objects.get(id=blog_post_id)

    context = {'blog': blog}
    return render(request, 'exercises/blog_post.html', context)


def timon(request):
    context = {}
    return render(request, 'exercises/timon.html', context)


def pumba(request):
    animal_name = request.POST['animal_name']
    animals = Animal.objects.filter(name__contains=animal_name)

    context = {'animals': animals}
    return render(request, "exercises/animal_search.html", context)

def marvel(request):
    context = { }
    return render(request, 'exercises/marvel.html', context)

def super_search(request):
    hero_name = request.POST['hero_name']
    superheroes = Superhero.objects.filter(name__contains=hero_name)
    results = len(superheroes)

    context = {'superheroes': superheroes, 'results' : results, 'hero_name' : hero_name }
    return render(request, 'exercises/hero_search.html', context)

def hero_entry(request, hero_entry_id):
    
    superhero = Superhero.objects.get(id=hero_entry_id)

    context = {'superhero' : superhero}
    return render(request, 'exercises/hero_entry.html', context)

def friend_list(request):
    all_friends = Friend.objects.all()
    
    context = { 'all_friends': all_friends }
    return render(request, "exercises/friend_list.html", context)

def friend_save(request):
   friend_name = request.POST["full_name"]
   friend = Friend.objects.create(name=friend_name)

   return HttpResponseRedirect(reverse('exercises:friend_list'))

def graffiti(request):
  graffitis = Graffiti.objects.all()

  context = { 'graffitis' : graffitis }
  return render(request, 'exercises/graffiti.html', context)

def graffiti_save(request):
  author = request.POST['author']
  wall_message = request.POST['message']
  graffiti = Graffiti.objects.create(name=author, message=wall_message)

  return HttpResponseRedirect(reverse('exercises:graffiti'))

def foods(request):
  foods = Food.objects.all()

  context = { 'foods' : foods }
  return render(request, 'exercises/food.html', context)

def food_save(request):
  food_name = request.POST['food_name']
  foods = Food.objects.create(name=food_name)

  return HttpResponseRedirect(reverse('exercises:foods'))

def food_entry(request, food_entry_id):
    
  food = Food.objects.get(id=food_entry_id)

  context = {'food' : food, 'food_entry_id' : food_entry_id}
  return render(request, 'exercises/food_entry.html', context)

def food_edit(request, food_entry_id):
  food = Food.objects.get(id=food_entry_id)
  food.name = request.POST['food_name']
  food.save()

  return HttpResponseRedirect(reverse('exercises:foods'))

def phone_book(request):
  if 'phone_name' in request.GET:
    contacts = Phone.objects.filter(name__contains=request.GET['phone_name']).order_by(Lower('name'))
  else:
    contacts = Phone.objects.all().order_by(Lower('name'))

  context = { 'contacts' : contacts }
  return render(request, 'exercises/phone_book.html', context)

def phone_add(request):

  context = { }
  return render(request, 'exercises/phone_add.html', context)

def phone_form(request):
  name = request.POST['name']
  number = request.POST['number']
  address = request.POST['address']
  phone = Phone.objects.create(name=name, number=number, address=address)
  
  return HttpResponseRedirect(reverse('exercises:phone_book'))

def phone_entry(request, phone_entry_id):  
  phone = Phone.objects.get(id=phone_entry_id)

  context = {'phone' : phone, 'phone_entry_id' : phone_entry_id}
  return render(request, 'exercises/phone_entry.html', context)

def phone_edit_form(request, phone_entry_id):
  phone = Phone.objects.get(id=phone_entry_id)

  context = { 'phone' : phone }
  return render(request, 'exercises/phone_edit_form.html', context)

def phone_edit(request, phone_entry_id):
  phone = Phone.objects.get(id=phone_entry_id)
  phone.name = request.POST['name']
  phone.number = request.POST['number']
  phone.address = request.POST['address']
  phone.save()

  return HttpResponseRedirect(reverse('exercises:phone_book'))

def phone_delete(request, phone_id):
  phone = Phone.objects.get(id=phone_id)
  phone.delete()

  return HttpResponseRedirect(reverse('exercises:phone_book'))

def athletes(request):
  athletes = Athlete.objects.all().order_by('sport', 'name')

  context = { 'athletes' : athletes }
  return render(request, 'exercises/athletes.html', context)

def athlete_save(request):
  name = request.POST["name"]
  sport = request.POST["sport"]
  athlete = Athlete.objects.create(name=name, sport=sport)

  return HttpResponseRedirect(reverse('exercises:athletes'))

def athlete_delete(request, athlete_id):
  athlete = Athlete.objects.get(id=athlete_id)
  athlete.delete()

  return HttpResponseRedirect(reverse('exercises:athletes'))

def task_list(request):
  if 'task_item' in request.GET:
    task_list = Task.objects.filter(item__contains=request.GET['task_item']).order_by('-priority')
  else:
    task_list = Task.objects.all().order_by('-priority')

  context = { 'task_list' : task_list }
  return render(request, 'exercises/task_list.html', context)

def task_add(request):
  item = request.POST['item']
  priority = request.POST['priority']
  task = Task.objects.create(item=item, priority=priority)

  return HttpResponseRedirect(reverse('exercises:task_list'))

def task_delete(request, task_id):
  task = Task.objects.get(id=task_id)
  task.delete()

  return HttpResponseRedirect(reverse('exercises:task_list'))

def task_complete(request, task_id):
  task = Task.objects.get(id=task_id)
  if(task.is_complete == False):
    task.is_complete = True
    task.save()
  else:
    task.is_complete = False
    task.save()
  
  return HttpResponseRedirect(reverse('exercises:task_list'))

def task_edit_form(request, task_id):
  task = Task.objects.get(id=task_id)

  context = { 'task' : task }
  return render(request, 'exercises/task_edit_form.html', context)

def task_edit(request, task_id):
  task = Task.objects.get(id=task_id)
  task.item = request.POST['item']
  task.priority = request.POST['priority']
  task.save()

  return HttpResponseRedirect(reverse('exercises:task_list'))

def login_page(request):
  context = {}
  return render(request, 'exercises/auth-login.html', context)

def login_form(request):
  username = request.POST['username']
  password = request.POST['password']
  user = authenticate(request, username=username, password=password)
  if user is not None:
    login(request, user)
    return HttpResponseRedirect(reverse('exercises:private'))
  else:
    return HttpResponseRedirect(reverse('exercises:login_page'))
      # Return an 'invalid login' error message.


@login_required
def private(request):
    # return HttpResponse('Hello ' + str(request.user))

  context = {}
  return render(request, 'exercises/auth-private.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('exercises:login_page'))  

def public(request):
    context = {}
    return render(request, 'exercises/auth-public.html', context)

@login_required
def reset(request):
    context = {}
    return render(request, 'exercises/auth-recover.html', context)

@login_required
def reset_form(request):
  password1 = request.POST['password1']
  password2 = request.POST['password2']
  if password1 == password2:
    u = request.user
    u.set_password(password1)
    u.save()
    return HttpResponseRedirect(reverse('exercises:login_page'))
  else:
    return HttpResponseRedirect(reverse('exercises:reset'))


def registration(request):
    context = {}
    return render(request, 'exercises/auth-registration.html', context)

def registration_form(request):
  username = request.POST['username']
  email = request.POST['email']
  password = request.POST['password']
  user = User.objects.create_user(username, email, password)

  return HttpResponseRedirect(reverse('exercises:login_page'))

def pinboard(request):
  quotes= Pinboard.objects.order_by('created_at')

  context = { 'quotes' : quotes }
  return render(request, 'exercises/pinboard.html', context)

@login_required
def pin_quote_form(request):
  message = request.POST['quote']
  author = request.user
  quote = Pinboard.objects.create(message=message, author=author)

  return HttpResponseRedirect(reverse('exercises:pinboard'))

def pin_login(request):

  context = {}
  return render(request, 'exercises/pin_login.html', context)

def pin_login_form(request):
  username = request.POST['username']
  password = request.POST['password']
  user = authenticate(request, username=username, password=password)
  if user is not None:
    login(request, user)
    return HttpResponseRedirect(reverse('exercises:pinboard'))
  else:
    return HttpResponseRedirect(reverse('exercises:pin_login'))

def pin_registration(request):
    context = {}
    return render(request, 'exercises/pin_registration.html', context)

def pin_registration_form(request):
  username = request.POST['username']
  email = request.POST['email']
  password = request.POST['password']
  user = User.objects.create_user(username, email, password)

  return HttpResponseRedirect(reverse('exercises:pin_login'))

@login_required
def pin_change_password(request):
  context = {}
  return render(request, 'exercises/pin_change_password.html', context)

@login_required
def pin_change_password_form(request):
  old_password = request.POST['old_password']
  new_password = request.POST['new_password']
  confirm_password = request.POST['confirm_password']
  check = request.user.check_password(old_password)
  if check == True and new_password == confirm_password:
    u = request.user
    u.set_password(new_password)
    u.save()
    logout(request)
    return HttpResponseRedirect(reverse('exercises:pin_login'))
  else:
    return HttpResponseRedirect(reverse('exercises:pin_change_password'))

def pin_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('exercises:pinboard'))  