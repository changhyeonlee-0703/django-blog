from django.shortcuts import HttpResponse, render
from .model import BugerMaterial
from .forms import BugerForm
# Create your views here.


def buger(request):
    buger_all = BugerMaterial.objects.all()
    form = BugerForm()
    if request.method =='POST':
        form =BugerForm(request.POST)
        if form.is_valid():
            
            form.save()
    return render(request,"buger.html",{'buger_list':buger_all,'buger_form':form})

