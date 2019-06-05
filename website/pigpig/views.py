from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from pigpig.models import part
# Create your views here.

def pigpig(request):

    return render(request, 'pigpig/index.html')

def indexCut(request):

    return render(request, 'pigpig/index-cut.html')

def aa(request):
    a1 = part.objects.get(id=1)
    return render(request, 'pigpig/a.html',locals())

def bb(request):
    a1 = part.objects.get(id=2)
    return render(request, 'pigpig/b.html',locals())

def cc(request):
    a1 = part.objects.get(id=3)
    return render(request, 'pigpig/c.html',locals())

def dd(request):
    a1 = part.objects.get(id=4)
    return render(request, 'pigpig/d.html',locals())

def ee(request):
    a1 = part.objects.get(id=5)
    return render(request, 'pigpig/e.html',locals())

def ff(request):
    a1 = part.objects.get(id=6)
    return render(request, 'pigpig/f.html',locals())

def gg(request):
    a1 = part.objects.get(id=7)
    return render(request, 'pigpig/g.html',locals())

def hh(request):
    a1 = part.objects.get(id=8)
    return render(request, 'pigpig/h.html',locals())

def ii(request):
    a1 = part.objects.get(id=9)
    return render(request, 'pigpig/i.html',locals())

def jj(request):
    a1 = part.objects.get(id=10)
    return render(request, 'pigpig/j.html',locals())

def kk(request):
    a1 = part.objects.get(id=11)
    return render(request, 'pigpig/k.html',locals())
