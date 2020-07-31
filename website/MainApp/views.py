from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.contrib.auth.models import User
from . import db
from . import models
from django.contrib import auth
import pdb
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Room


# Create your views here.

def index(request):
	return render(request, 'MainApp/index.html')

def register(request):
	if request.user.is_authenticated:
		return render(request, 'MainApp/index.html')
	else:
		return render(request, 'MainApp/register.html')

def login(request):
	if request.user.is_authenticated:
		return render(request, 'MainApp/index.html')
	else:
		return render(request, 'MainApp/login.html')

def menu(request):
	if request.user.is_authenticated:
		return render(request, 'MainApp/menu.html')
	else:
		return render(request, 'MainApp/login.html')


@csrf_exempt
def hide_button(request):
    print('session',request.user)
    if request.user.is_authenticated:
        return JsonResponse({'status':True,'message':'True'}, status=200)
    else:
        return JsonResponse({'status':False,'message':'False'}, status=400)

@csrf_exempt
def logout(request):
    auth.logout(request)
    return render(request, 'MainApp/index.html', {'message':"1st page"})

@csrf_exempt
def signup(request):
    data = json.loads(request.body.decode('utf-8'))
    username = data.get('username')
    studentId = data.get('studentId')
    email=data.get('email')
    password=data.get('password')
    user_existed = User.objects.filter(username=username)
    if user_existed:
        user = models.login.objects.filter(user=user_existed[0])
        if user:
        	return JsonResponse({'status':'False','message':'Username Already Exist'}, status=400)
        else:
            login_user = models.login.objects.create_user(user_existed,studentId)
            login_user.save()
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                username=User.objects.get(username=username).pk
                request.session['username'] = username
				# pdb.set_trace()
                auth.login(request, user)
                return JsonResponse({'status':'true','message':'Registered Successfully'}, status=200)

    if (email and password  and studentId):
        saver=db.new_user_make(username,email,password)
        if (saver):
            login_user = models.login.objects.create_user(saver,studentId)
            login_user.save()
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                username=User.objects.get(username=username).pk
                request.session['username'] = username
				# pdb.set_trace()
                auth.login(request, user)
                return JsonResponse({'status':'true','message':'Registered Successfully'}, status=200)     

        else:
            return JsonResponse({'status':'False','message':'Problem Creating User'}, status=400) 

    
    else:
        return JsonResponse({'status':'False','message':'Please Fill All Details'}, status=400)

@csrf_exempt
def user_login(request):
    data = json.loads(request.body.decode('utf-8'))
    if not data:
        return JsonResponse({'status':'False','message':'No Data Received'}, status=400)
    username = data.get('username')
    password = data.get('password')
    UserData = User.objects.filter(is_staff=True, username=username)
    if UserData:
        user = auth.authenticate(username=username, password=password)
        if not user:
            return JsonResponse({'status':'false','message':'Incorrect Id Or Password'}, status=400)
        if user is not None:
            username=User.objects.get(username=username).pk
            request.session['username'] = username
            auth.login(request, user)
            return JsonResponse({'status':'true','message':'Logged In'}, status=200)
        else:
            return JsonResponse({'status':'false','message':'Not Authorised'}, status=400)
    else:
        user = auth.authenticate(username=username, password=password)
        if not user:
            return JsonResponse({'status':'false','message':'Incorrect Id Or Password'}, status=400)
        
        login_table = models.login.objects.filter(user=user)
        if not login_table:
            return JsonResponse({'status':'false','message':'Please Register Again'}, status=400)
        if user is not None:
            username=User.objects.get(username=username).pk
            request.session['username'] = username
            auth.login(request, user)
            return JsonResponse({'status':'true','message':'Logged In'}, status=200)
        else:
            return JsonResponse({'status':'false','message':'Not Authorised'}, status=400)

def chat(request):
    if request.user.is_authenticated:
            rooms = Room.objects.order_by("title")
            print(rooms)
            print(request.user.id)
            return render(request, "chat.html", {"rooms": rooms,"userid":request.user.id})
    else:
        return render(request, 'MainApp/login.html')



@csrf_exempt
def get_category(request):
    category_data = db.get_category_data()
    return JsonResponse({'status':'true','message':category_data}, status=200)

@csrf_exempt
def get_product(request):
    product_data = db.get_product_data()
    return JsonResponse({'status':'true','message':product_data}, status=200)

@csrf_exempt
def update_products(request):
    data = json.loads(request.body.decode('utf-8'))
    if not data:
        return JsonResponse({'status':'False','message':'No Data Received'}, status=400)
    for i in data['data']:
        productId = i.get('id')
        quantity = i.get('quantity')
        current_quantity = i.get('current_quantity')
        new_quantity = quantity - current_quantity
        productData = models.products.objects.filter(id=productId)
        if productData:
            productData[0].quantity = new_quantity
            productData[0].save()
        else:
            return JsonResponse({'status':'False','message':'Problem in Updating Products'}, status=400)
    return JsonResponse({'status':'true','message':'Products Data Updated'}, status=200)