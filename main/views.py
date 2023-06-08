from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User

# Create your views here.
def index(request):
  return render(request, 'index.html')


def skills(request):
  return render(request, 'skills.html')


def about(request):
  return render(request, 'about.html')


def products(request):
  return render(request, 'products.html')