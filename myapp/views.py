from django.shortcuts import render , get_object_or_404,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
# Create your views here.


def index(request):
    entries = Entry.objects.all()
    return render(request , 'myapp/index.html',{'entries':entries})
@login_required
def calender(request):
    entries = Entry.objects.filter(author=request.user)
    return render(request , 'myapp/calender.html',{'entries':entries})

def details(request, pk):
    entry = Entry.objects.get(id=pk)
    return render(request, 'myapp/details.html', {'entry':entry})
@login_required
def add (request):
    if request.method == 'POST':
        form =EntryForm(request.POST)
        if form.is_valid():

            ###
            name = form.cleaned_data['name']
            date = form.cleaned_data['date']
            description = form.cleaned_data['description']
            lacations=form.cleaned_data['lacations']

            Entry.objects.create(
                author=request.user,
                name=name,
                date=date,
                description=description,
                lacations=lacations,
            ).save()

            return HttpResponseRedirect('/calender')

    else:
        form =EntryForm()

    return render(request, 'myapp/forms.html', {'form':form})
@login_required
def delete (request, pk):

    if request.method == 'DELETE':
        entry = get_object_or_404(Entry, pk=pk)
        entry.delete()
    return HttpResponseRedirect('/')
@login_required
def hapus (request, id:None):
    hapus =get_object_or_404(Entry, id=id)
    hapus.delete()
    return redirect ("index")

def signup(request):
    if request.method == 'POST':
        form= UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password1'],
            firstname = form.cleaned_data['firstname'],
            lastname = form.cleaned_data['lastname'],
            user= authenticate(username=username,password=password,lastname=lastname, firstname =firstname)
            login(request, user)
            return redirect ('/calender')
    else:
        form = UserCreationForm()
    return render(request,'registration/signup.html',{'form':form})
