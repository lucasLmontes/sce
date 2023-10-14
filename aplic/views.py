from django.shortcuts import render
from aplic.models import Produto

def index(request):
    obj=Produto.objects.all()
    context={
        'obj':obj,
        }
    return render(request, 'index.html', context)
