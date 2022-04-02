# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
  item = models.CharField(max_length = 200)
  priority = models.IntegerField()
  is_complete = models.BooleanField(default=False)

  def __str__(self):
    return self.item

class Athlete(models.Model):
  name = models.CharField(max_length = 100)
  sport = models.CharField(max_length = 50)

  def __str__(self):
    return self.name

class Phone(models.Model):
  name = models.CharField(max_length = 100)
  number = models.CharField(max_length = 20)
  address = models.CharField(max_length = 200)

  def __str__(self):
    return self.name

class Food(models.Model):
  name = models.CharField(max_length = 100)

  def __str__(self):
    return self.name

class Graffiti(models.Model):
  message = models.CharField(max_length = 600)
  name = models.CharField(max_length = 50)

  def __str__(self):
    return self.message

class Friend(models.Model):
  name = models.CharField(max_length = 200)

  def __str__(self):
    return self.name

class Blog(models.Model):
  title = models.CharField(max_length = 200)
  body = models.CharField(max_length = 200)

  def __str__(self):
    return self.title

class Credit(models.Model):
  number = models.CharField(max_length=50)
  card = models.CharField(max_length=200)
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name

class Employee(models.Model):
  employee = models.CharField(max_length=200)
  dept = models.CharField(max_length=200)
  salary = models.FloatField()

  def __str__(self):
    return self.employee

class Message(models.Model):
    text = models.CharField(max_length=200)
    is_hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class Superhero(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    superpower = models.CharField(max_length=100)
    is_good = models.BooleanField()
    is_male = models.BooleanField()
    rating = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.name
        
        

class Animal(models.Model):
    name = models.CharField(max_length=100)
    birthplace = models.CharField(max_length=200)
    is_male = models.BooleanField()
    
    def __str__(self):
        return self.name 
        

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    
    def __str__(self):
        return self.make + " " + self.model + " " + str(self.year)
    
class Stock(models.Model):
    company = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    market_cap = models.FloatField()
    
    def __str__(self):
        return self.company
        

class Artist(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
        
    
class Song(models.Model):
    name = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name



class Country(models.Model):
    name = models.CharField(max_length=255)
    population = models.IntegerField()
    
    def __str__(self):
        return self.name
        
    
class City(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, default=83)
    
    def __str__(self):
        return self.name



class NBATeam(models.Model):
    name = models.CharField(max_length=255)
    worth = models.IntegerField()
    
    def __str__(self):
        return self.name
        
    
class NBAAthlete(models.Model):
    name = models.CharField(max_length=255)
    team = models.ForeignKey(NBATeam, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Owner(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
      return self.name

class Pet(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    
    def __str__(self):
      return self.name

class Museum(models.Model):
  name=models.CharField(max_length=255)

  def __str__(self):
    return self.name

class Art(models.Model):
  name = models.CharField(max_length=255)
  museum = models.ForeignKey(Museum, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

class Award(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
    return self.name

class Winner(models.Model):
  name = models.CharField(max_length=255)
  year = models.IntegerField()
  award = models.ForeignKey(Award, on_delete=models.CASCADE)

  def __str__(self):
    return self.name + ' (' + str(self.year) + ')'

class Pinboard(models.Model):
  message = models.TextField()
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.message
  