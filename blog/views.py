# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django import forms
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
# Create your views here.
from .models import User, Article
from datetime import datetime


class UserForm(forms.Form):
    username = forms.CharField()
    # password = forms.CharField(widget=forms.PasswordInput)
    headImag = forms.FileField()


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            path = './tmp/upload/' + str(uuid.uuid4()) + '.jpg';
            fp = open(path, 'wb')
            s = form.cleaned_data['headImag'].read()
            fp.write(s)
            fp.close()
            user = User.objects.create(
                username=form.cleaned_data['username'],
                headImag=path
            )

            return HttpResponse(serializers.serialize("json", [user]))
    else:
        return render_to_response('register.html', {'form': UserForm()})


def detail(request, num):
    post = Article.objects.all()[int(num)]
    Str = "title=%s, category=%s, date_time=%s, content=%s" % (post.title, post.category, post.date_time, post.content)

    return HttpResponse(Str)


def test(request):
    return render(request, 'test.html', {'current_time': datetime.now()})


def home(request):
    post_list = Article.objects.all()
    return render(request, 'home.html', {'post_list': post_list})
