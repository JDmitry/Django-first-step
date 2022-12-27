from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

rick = Person(name="Rick", age=45)
rick.save()