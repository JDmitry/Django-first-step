from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

all = Person.objects.all()

for i in all:
    print(i.name)