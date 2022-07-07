from django.shortcuts import render
from . models import Lead, Agent, User

def view(request):
    return render(request, 'leads-view.html',{})
