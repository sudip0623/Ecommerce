from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'Homeapp/home.html')

def account(request):
    return render(request, 'Homeapp/account.html')

def deals(request):
    return render(request, 'Homeapp/deals.html')

def help(request):
    return render(request, 'Homeapp/help.html')

def registry(request):
    return render(request, 'Homeapp/registry.html')

def sell(request):
    return render(request, 'Homeapp/sell.html')
