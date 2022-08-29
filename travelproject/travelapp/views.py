from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import Team


# Create your views here.


def demo(request):
    obj = Place.objects.all()
    objj = Team.objects.all()
    return render(request, "index.html", {'result': obj, 'results': objj})
#
# def about(request):
#     return render(request, "about.html")
#
# def contact(request):
#     return render(request, "contact.html")
#
# def home(request):
#     return render(request, "home.html")
#
# def details(request):
#     return render(request, "details.html")
#
# def Thanks(request):
#     return HttpResponse("Thank You")
