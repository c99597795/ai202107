from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import random
from plotly.offline import plot
import plotly.graph_objs as go
import numpy as np

from mysite.models import Post,Country,City,Note

# Create your views here.
def index(request):
    names = "張世群"
    lotto = [random.randint(1,42) for i in range(6)]
    special = lotto[0]
    lotto=lotto[1:6]
    x = np.linspace(-6*np.pi,6*np.pi,360)
    y1 = np.sin(x)
    y2 = np.cos(x)
    plot_div = plot([go.Scatter(x=x, y=y1,
		mode='lines', name='SIN', text="Title",
		opacity=0.8, marker_color='blue'),
		go.Scatter(x=x, y=y2,
		mode='lines', name='COS', 
		opacity=0.8, marker_color='green')],
		output_type='div')
    return render(request,"index.html",locals())
def news(request):
    posts = Post.objects.all()
    return render(request,"news.html",locals())
@login_required(login_url="/admin/login/")
def show(request, id):
    try:
        post = Post.objects.get(id=id) #找出符合條件的第一個紀錄
    except:
        return redirect("/news/")
    return render(request,"show.html",locals())
@login_required(login_url="/admin/login/")
def rank(request):
    if request.method == 'POST':
        id = request.POST["id"]
        try:
            country = Country.objects.get(id=id)
        except:
            redireact("/rank/")
        cities = City.objects.filter(country = country)
    else:
        cities = City.objects.all()
    countries = Country.objects.all()
    return render(request,"rank.html",locals())
@login_required(login_url="/admin/login/")
def chart(request):
    if request.method == 'POST':
        id = request.POST["id"]
        try:
            country = Country.objects.get(id=id)
            cities = City.objects.filter(country = country)
        except:
            cities = City.objects.all()
    else:
        cities = City.objects.all()
    countries = Country.objects.all()
    names = [city.name for city in cities]
    population = [city.population for city in cities]
    return render(request,"chart.html",locals())
def mylogout(request):
    logout(request)
    return redirect("/")
def delete(request,id):
    try:
        post=Post.objects.get(id=id)
        post.delete()
    except:
        return redirect("/news/")
    return redirect("/news/")
def deletenote(request,id):
    try:
        note=Note.objects.get(id=id)
        note.delete()
    except:
        return redirect("/note/")
    return redirect("/note/")
def addnote(request):
    if request.method == 'POST':
        title=request.POST["note"]
        if len(title) > 10:
            note = Note(title=title)
            note.save()
    return redirect("/note/")
def note(request):
    notes = Note.objects.all()
    return render(request,"note.html",locals())