from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import random
def index(request):
    names = "張世群"
    lotto = [random.randint(1,42) for i in range(6)]
    special = lotto[0]
    lotto=lotto[1:6]
    return render(request,"index.html",locals())