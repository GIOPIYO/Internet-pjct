from django.shortcuts import render
from django.http import HttpResponse

def index(request):
   return render(request,"farmlease/templates/index.html")
    
def about(request):
    return render(request, "farmlease/templates/about.html")
 
def catalog(request):
    return render(request, "farmlease/templates/catalog.html")
 
def catalog1(request):
    return render(request, "farmlease/templates/catalog1.html")
 
def contacts(request):
    return render(request,"farmlease/templates/contacts.html")
 
def prodDetails(request):
    return render(request,"farmlease/templates/prodDetails.html")