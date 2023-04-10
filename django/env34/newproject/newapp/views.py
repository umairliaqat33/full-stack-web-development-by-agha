from django.shortcuts import render, HttpResponse

# Create your views here.


def agha(request):
    return HttpResponse("Welcomeavxabhcxaxha")


def umair(request):
    return render(request, 'About.html')
