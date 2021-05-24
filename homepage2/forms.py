
from django import forms
from .model import BugerMaterial

class BugerForm(forms.ModelForm):
    class Meta :
        model = BugerMaterial
        fields = ('type', 'brend_name', 'director_name', 'price', 'stock', 'is_set')#'brend_name', 'director_name', 'price'