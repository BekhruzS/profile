from django.shortcuts import render, get_object_or_404, redirect


def home(request):

    return render(request, 'home.html')

def about(request):

    return render(request, 'about.html')

def contactt(request):

    return render(request, 'contact.html')








