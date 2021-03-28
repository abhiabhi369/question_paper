from django.shortcuts import render

def home(request):
    return render(request,'paper_app/home.html')