
from django.shortcuts import render , redirect
from django.contrib import messages
from .forms import *
from .models import *


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            all_items = TodoModel.objects.all()
            context = {
                'all_items' : all_items
            }
            messages.success(request,('item has been added'))
            return render(request , 'templates/home.html' , context=context)
    else :
        all_items = TodoModel.objects.all()
        context = {
            'all_items':all_items
        }
        return render(request , 'templates/home.html' , context=context)


def delete(request , list_id):
    item_delete= TodoModel.objects.get(pk=list_id)
    item_delete.delete()
    messages.success(request , ('item has been deleted'))
    return redirect('home')