from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):
    
    dest = Destination.objects.all()
    
    return render(request, 'index.html', {'dest': dest})


def about(request):
    
    destt = Destination.objects.all()
    
    return render(request, 'about.html', {'destt': destt})



from django.shortcuts import render
from .models import Destination

def product(request):
    destinations = Destination.objects.all()
    context = {'destinations': destinations}
    return render(request, 'product.html', context)

