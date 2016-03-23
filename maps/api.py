import json

from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

import googlemaps

from maps.models import Pointer
from maps.forms import MarkedPointerForm


@csrf_exempt
@require_POST
def store_point(request):
    form = MarkedPointerForm(request.POST)
    if form.is_valid():
        # Get gmap client with proper API KEY
        gmap = googlemaps.Client(key=settings.GMAP_API_KEY)
        # Clean the data
        data = form.cleaned_data
        latitude = data['latitude']
        longitude = data['longitude']
        print data
        # Get the location information from google maps API
        location_info = gmap.reverse_geocode((latitude, longitude))
        # Check if the location has any address
        try:
            address = location_info[0]['formatted_address']
            # Save the address and geocode information
            form.save(address=address)
            # Return the address in json
            info = json.dumps({'address':address})
            return HttpResponse(info, status=201)
        except IndexError:
            pass
        except KeyError:
            pass
        return HttpResponse(status=404)

    return HttpResponse(status=400)

