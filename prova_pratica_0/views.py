from django.shortcuts import render

def index1(request):
    return render(request, "index1.html")

def somma(request):
    import random
    var1 = random.randint(1, 10)
    var2 = random.randint(1, 10)
    context = {
        'var1' : var1,
        'var2' : var2,
        'somma' : var1 + var2,
    }
    return render(request, "somma.html", context)

def media(request):
    import random
    vet1 = []
    somma = 0
    for i in range(0, 30):
        num = random.randint(1, 10)
        somma += num
        vet1.append(num)
    media = somma/30
    
    context = {
        'vet1' : vet1,
        'media' : media,
    }
    return render(request, "media.html", context)
