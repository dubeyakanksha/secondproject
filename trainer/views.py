from django.shortcuts import render,HttpResponse

def index(request):
    return render(request,'index.html')

def charts(request):
    return render(request,'charts.html')

def documentataions(request):
    return render(request,'documentations.html')

def dropdowns(request):
    return render(request,'dropdowns.html')

def forms(request):
    return render(request,'forms.html')

def icons(request):
    return render(request,'icons.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def tables(request):
    return render(request,'tables.html')

def typography(request):
    return render(request,'typography.html')

def buttons(request):
    return render(request,'buttons.html')
