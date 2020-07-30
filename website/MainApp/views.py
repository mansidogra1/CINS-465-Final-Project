from django.shortcuts import render
#from django.http import HttpResponse
import sqlite3
# Create your views here.

def index(request):
	return render(request, 'MainApp/index.html')

def register(request):
	return render(request, 'MainApp/register.html')

def login(request):
	if request.method == "POST":
		username = request.POST.get('username')
	return render(request, 'MainApp/login.html')

