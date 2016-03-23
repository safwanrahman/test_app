from django.conf import settings
from django.shortcuts import render

from maps.models import Pointer

def maps(request):
    data = {
        'gmap_key': settings.GMAP_API_KEY
    }

    # Discard all the object if discard button is clicked
    if request.GET.get('discard'):
        Pointer.objects.all().delete()

    return render(request, 'maps.html', data)