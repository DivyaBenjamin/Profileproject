from django.shortcuts import render,redirect
from Profile.models import *

# Create your views here.
def Profile(request):
    return render(request,'Profile/Profile.html') 