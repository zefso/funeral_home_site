from django.shortcuts import render, get_object_or_404
from services.models import Service, Category

def home(request):
    services = Service.objects.filter(is_active=True)[:3]
    return render(request, 'core/home.html', {'services': services})

def service_list(request):
    categories = Category.objects.all()
    services = Service.objects.filter(is_active=True)
    return render(request, 'core/service_list.html', {'categories': categories, 'services': services})

def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'core/service_detail.html', {'service': service})

def contact(request):
    return render(request, 'core/contact.html')

def precaution(request):
    return render(request, 'core/precaution.html')

def funeral_speeches(request):
    return render(request, 'core/funeral_speeches.html')

def farewell(request):
    return render(request, 'core/farewell.html')
