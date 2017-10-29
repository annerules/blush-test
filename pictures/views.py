from django.shortcuts import render
from django.http import HttpResponse
from .models import Logo_and_icons
from .models import Main_pic
from django.shortcuts import get_object_or_404
# Create your views here.
def main_page(request) :
    return render(request, 'pictures/base.html')
