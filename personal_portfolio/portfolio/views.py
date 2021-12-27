from django.shortcuts import render

# Create your views here.
def home(request):
    """
    A function that returns text back to the user.
    """
    return render(request,'blog/my_portfolio.html', {'home':home})