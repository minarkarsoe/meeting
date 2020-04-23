# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from  .models import Meeting , Room

def detail(request,id):
    metting = get_object_or_404(Meeting,pk=id)
    return render(request, "mettings/detail.html", {"metting" : metting})

def room_list(request):
    return render(request, "mettings/room.html", 
                    { "rooms" : Room.objects.all() })

# Create your views here.
