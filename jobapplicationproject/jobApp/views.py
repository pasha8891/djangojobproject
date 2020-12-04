from django.shortcuts import render
from jobApp.models import *

# Create your views here.
def index(request):
    return render(request,'jobApp/index.html')

def hydjobs1(request):
    jobs_list=hydjobs.objects.order_by('date')
    my_dict={'jobs_list':jobs_list}
    return render(request,'jobApp/hydjobs.html',context=my_dict)

def mumbaijobs(request):
    return render(request,'jobApp/mumbaijobs.html')

def punejobs(request):
    return render(request,'jobApp/punejobs.html')

def chennaijobs(request):
    return render(request,'jobApp/chennaijobs.html')
