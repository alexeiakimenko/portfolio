from django.shortcuts import render, get_object_or_404
from .models import Places
from django.contrib.auth.decorators import login_required


@login_required
def places(request):
    place = Places.objects.all()
    return render(request, 'places/places.html', {'places': place})


@login_required
def details(request, place_id):
    place = get_object_or_404(Places, pk=place_id)

    return render(request, 'places/details.html', {'place': place})
