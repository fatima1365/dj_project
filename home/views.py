from django.shortcuts import render

# Create your views here.

def home_func(request):
    return render(request, 'home/home_page.html')


