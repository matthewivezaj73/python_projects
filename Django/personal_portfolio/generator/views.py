from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    """
    A function that returns text back to the user.
    """
    return render(request,'generator/home.html', )
