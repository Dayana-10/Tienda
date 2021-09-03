from django.shortcuts import render

# Create your views here.
def Tienda(request):
    return render(request, 'Index1.html')

def Dulces(request):
    return render(request, 'pagina2.html')