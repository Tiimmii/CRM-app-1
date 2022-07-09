from django.shortcuts import render,redirect
from . models import Lead, Agent, User
from . forms import LeadCreateForm
from django.contrib import messages

def view(request):
    lead = Lead.objects.all()
    return render(request, 'leads-view.html', {'lead':lead})

def details(request, pk):
    lead = Lead.objects.get(id=pk)
    return render(request, 'leads-details.html', {'lead':lead})

def create(request):
    form = LeadCreateForm()
    
    if request.method == 'POST':
        form=LeadCreateForm(request.POST)
        if form.is_valid():
            form.save()    
            return redirect('leads:view')
        else:
            messages.info('unsuccessful :(')
            return redirect('leads:create')
    
    else:
        return render(request, 'leads-create.html', {'form':form})
