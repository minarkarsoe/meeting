# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Meeting,Room

admin.site.register(Meeting)
admin.site.register(Room)
# Register your models here.
