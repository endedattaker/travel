from django import forms
from .models import Booking
from .models import Packages

class Bookingform(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'
    '''def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add a queryset to the place field to populate it with package places
        self.fields['place'].queryset = Packages.objects.all()'''
    