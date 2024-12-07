from django.shortcuts import render
from .models import Agent,Tester
# Create your views here.
def home(request):
    return render(request,'root/index.html')

def agent(request):
    agents = Agent.objects.filter(status=True)
    context = {
        'agents':agents
    }
    return render(request,'root/agents.html',context=context)

def contact(request):
    return render(request,'root/contact.html')

def about(request):
    return render(request,'root/about.html')
