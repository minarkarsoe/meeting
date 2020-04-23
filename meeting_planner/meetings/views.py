# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,get_object_or_404 ,redirect
from  .models import Meeting , Room
from .form import MeetingForm

def detail(request,id):
    metting = get_object_or_404(Meeting,pk=id)
    return render(request, "mettings/detail.html", {"metting" : metting})

def room_list(request):
    return render(request, "mettings/room.html", 
                    { "rooms" : Room.objects.all() })

def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:    
        form = MeetingForm()
    return render(request, "mettings/new.html",{"form":form})

# Create your views here.
