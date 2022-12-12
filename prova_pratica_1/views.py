from django.shortcuts import render

def index2(request):
    return render(request,"index2.html") 

def view_a(request):
     context= {
        'list1':["Matematica", "Italiano", "Inglese", "Storia", "Geografia"]
     }
     return render(request, "view_a.html",context)

def view_b(request):
    return render(request,"view_b.html")

def view_c(request):
    return render(request,"view_c.html")
