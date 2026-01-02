from django.shortcuts import render,HttpResponseRedirect,redirect
from .forms import DoctorRegisteration
from .models import User,Doctor

#login logout signup
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from django.template.loader import render_to_string
from django.conf import settings
# otp verfication
import random
from django.core.cache import cache
from twilio.rest import Client

# ajex crud
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Item
from .forms import ItemForm



# Create your views here.
@login_required
def add_doc(request):
    if request.method == 'POST':
        fm=DoctorRegisteration(request.POST)
        
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg =User(name=nm,email=em,password=pw)
            reg.save()
            fm=DoctorRegisteration()
            # fm.save()
    else:
        fm=DoctorRegisteration()
    stud=User.objects.all()
    
    return render(request,'enroll/add_doc.html',{'form':fm,'stu':stud})

def delete_data(request, id):
    if request.method == 'POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return  HttpResponseRedirect('/')
    
def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm=DoctorRegisteration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm=DoctorRegisteration(instance=pi)
    return render(request,'enroll/update_doc.html',{'form':fm})


#login logout signup

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'

            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'enroll/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'enroll/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def home_view(request):
    return render(request, 'enroll/home.html')


# js validation
def javascript_validation(request):
    return render(request,'enroll/javascript_validation.html')

def generate_otp():
    return str(random.randint(100000, 999999))


def send_sms(request):
    phone_number = "+917779009972"
    otp = generate_otp()
    print(otp)
    
    # Store OTP in cache for 5 minutes
    cache.set(phone_number, otp, timeout=300)
   
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=f'Your OTP is {otp}',
        from_=settings.TWILIO_PHONE_NUMBER,
        to=phone_number
    )
   
    return JsonResponse({'message': 'OTP sent successfully'})

# ajex crud

def item_list(request):
    items = Item.objects.all()
    return render(request, 'enroll/item_list.html', {'items': items})


def item_create(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            return JsonResponse({"id": item.id, "name": item.name, "description": item.description})
    return JsonResponse({"error": "Invalid data"}, status=400)


def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            return JsonResponse({"id": item.id, "name": item.name, "description": item.description})
    return JsonResponse({"message": "Item Edited"})


def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    return JsonResponse({"message": "Item deleted"})
