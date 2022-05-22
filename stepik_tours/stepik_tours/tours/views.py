from django.shortcuts import render
from django.http import HttpResponseNotFound,  HttpResponseServerError


# Create your views here.
def main_view(request):
    return render(request, "index.html")


def departure_view(request, departure):
    return render(request, "departure.html")


def tour_view(request, id):
    return render(request, "tour.html")


def custom_handler404(request, exception):
    # Call when Http404 raised
    return HttpResponseNotFound('Ресурс не найден!')


def custom_handler500(request):
    # Call when raised some python exception
    return HttpResponseServerError('Ошибка сервера!')
