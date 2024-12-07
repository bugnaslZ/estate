from django.shortcuts import render
from .models import Service
# Create your views here.
def service(request,**kwargs):
    if kwargs.get('cat') :
        service = Service.objects.filter(cat__name=kwargs.get('cat'))
    context = {
        'services':service
    }

    return render(request,'service/services.html',context=context)

def service_detail(request):
    id = request.GET.get('id')
    service = Service.objects.get(id=id)
    context = {
        'services':service
    }


    return render(request,'service/service-details.html',context=context)