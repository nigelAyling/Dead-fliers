from django.shortcuts import render, redirect
from .models import Airmen
from django.http import HttpResponse
from .forms import AirmenForm

def search_list(request):
    return render(request,'searches/search_list.html')
    

def CreateView(request):
    if request.method =='Post':
        form = AirmenForm(request.Post)
        if form.is_valid():
            form.save()
            return redirect('/data')
    else:
        form=AirmenForm()
        context = {
            'form':form
        }
        return render(request,'searches/create.html',context)



