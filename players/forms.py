from django import forms
from .models import Player

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'age', 'position', 'height', 'weight', 'image', 'biography']
