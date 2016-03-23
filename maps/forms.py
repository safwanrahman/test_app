from django import forms

from maps.models import Pointer


class MarkedPointerForm(forms.ModelForm):

    class Meta(object):
        model = Pointer
        fields = ('latitude', 'longitude')

    def save(self, address):
        geocode = self.cleaned_data
        pointer, created = Pointer.objects.get_or_create(address=address, **geocode)
        return pointer