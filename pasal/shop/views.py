from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render(request, 'base.html')
    # return HttpResponse("<h1 align='text-center'>Grand Technology Solution PVT LTD WEBAPP Update will be available here until we hosted it.</h1>")