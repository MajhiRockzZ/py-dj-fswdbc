from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def help(request):
    helpdict = {'help_insert': "HELP PAGE"}
    return render(request, 'appTwo/help.html', context=helpdict)
