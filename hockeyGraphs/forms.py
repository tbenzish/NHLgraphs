from django.forms import ModelForm, TextInput
from .models import Player

class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ['fullName']
        widgets = {'fullName' : TextInput(attrs={'class' : 'input', 'placeholder' : 'Player Name'})}