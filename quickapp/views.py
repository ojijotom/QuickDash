from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def About(request):
    return render(request,'About.html')
def gallery(request):
    return render(request,'gallery.html')