from django.shortcuts import render

# Create your views here.
def Tienda(request):
    return render(request, 'index.html')

def shoes(request):
    return render(request, 'shoes.html')

def contact(request):
    return render(request, 'contact.html')

def collection(request):
    return render(request, 'collection.html' )

def testimonial(request):
    return render(request, 'testimonial.html')

def racingboots(request):
    return render(request, 'racingboots.html')