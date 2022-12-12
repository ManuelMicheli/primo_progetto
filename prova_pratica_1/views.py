from django.shortcuts import render

def index2(request):
    return render(request,"index2.html") 

def view_a(request):
    return render(request,"view_a.html")

def view_b(request):
    return render(request,"view_b.html")

def view_c(request):
    return render(request,"view_c.html")
