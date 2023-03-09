from django.shortcuts import render
from django.http import HttpResponse

def nkr(request):
    return HttpResponse('<h1>No Data Found</h1>')
