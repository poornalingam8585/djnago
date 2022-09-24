from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404
from django.http import HttpResponse
from datetime import datetime , date

# Create your views here.

def index(request):
	return render(request,"index.html",locals())
