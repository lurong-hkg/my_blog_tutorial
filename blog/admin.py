# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.fro
from django.contrib import admin
from .models import User, Article

admin.site.register(User)
admin.site.register(Article)