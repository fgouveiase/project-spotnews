from django import forms
from .models.category_model import Categories


class CreateForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = "__all__"
