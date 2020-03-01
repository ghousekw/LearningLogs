from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import List
from .forms import ListForm
# to pass messages we use messages modules
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        form =  ListForm(request.POST or None)
        # if form is valid, save the form and list all objects present in our database in html
        if form.is_valid():
            form.save()
            all_items = List.objects.all()
            # passing a message that a list has been added successfully
            messages.success(request, 'Item has been added to a list')
            return render(request, 'home.html', {'all_items': all_items})
    
    else:
        all_items = List.objects.all()
        return render(request, 'home.html', {'all_items': all_items})

# Todo: delete an item from a list
def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item has benn deleted'))
    return redirect('home')

def strike_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')

def unstrike(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')

def edit(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)

        form =  ListForm(request.POST or None, instance=item)

        # if form is valid, save the form and list all objects present in our database in html
        if form.is_valid():
            form.save()
            # passing a message that a list has been added successfully
            messages.success(request, 'Item has been edited')
            return redirect('/home/')
    
    else:
        item = List.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item': item})

def search(request):
    qs = List.objects.all()
    item_name = request.GET.get('item_name')
    
    if item_name != '' and item_name is not None:
        qs = qs.filter(item__contains=item_name)
        
    context = {
        'queryset': qs
    }
    return render(request, 'home.html', context)