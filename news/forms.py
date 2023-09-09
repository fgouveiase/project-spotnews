from django import forms
from .models.category_model import Categories
from news.models.news_model import News


class CreateForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ["name"]

    name = forms.CharField(label="Nome", max_length=200)


class NewsFormCreate(forms.ModelForm):
    class Meta:
        model = News
        fields = [
            "title",
            "content",
            "author",
            "created_at",
            "image",
            "categories",
        ]
