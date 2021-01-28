from django import forms
from .models import MovieModel
from django.forms import ModelForm

class MovieForm(forms.ModelForm):
    class Meta:
        model = MovieModel
        fields = "__all__"


