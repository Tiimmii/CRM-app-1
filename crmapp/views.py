from django.shortcuts import render
from . models import Lead, Agent, User
from . forms import LeadCreateForm
def view(request):
    lead = Lead.objects.all()
    return render(request, 'leads-view.html',{lead:lead})
