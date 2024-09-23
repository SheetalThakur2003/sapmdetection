from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponse
import logging


# Create your views here.

def index(request):
    return render(request, 'index.html')


def download(request):
    return render(request, 'download.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')
