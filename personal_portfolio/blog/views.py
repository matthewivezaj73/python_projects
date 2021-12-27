from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    """
    A function that returns text back to the user.
    """
    return render(request, 'personal_portfolio/my_portfolio.html')
    
def about(request):
    """
    A function that returns text back to the user.
    """
    return render(request,'generator/about.html', {'about':about})