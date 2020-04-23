# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from meetings.models import Meeting 

# Create your views here.
def welcome(request):
    return render(request,"website/welcome.html",
                    {"meetings": Meeting.objects.all()})

def date(request):
    return HttpResponse("Server run time is ="+ str(datetime.now()))

def about(request):
    return HttpResponse("Hello lat say pyi pyi lr")