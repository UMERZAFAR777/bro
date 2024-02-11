from django.http import HttpResponse
from django.shortcuts import render,redirect
from app.models import Slider,Banner,Main_Categroy


def base(request):
    return render (request,'base.html')


def home (request):
    sliders = Slider.objects.all()
    banners = Banner.objects.all()
    main_categroy = Main_Categroy.objects.all()
    context = {
        'sliders':sliders,
        'banners':banners,
        'main_categroy': main_categroy,
    }
    return render (request,'home.html',context)





