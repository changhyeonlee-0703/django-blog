from django.shortcuts import render

# Create your views here.

def monthly_EDA_view(request):
    return render(request,'monthly_EDA.html',{})