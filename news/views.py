from django.shortcuts import render, redirect
from news.models.category_model import Categories
from .models.news_model import News
from news.forms import CreateForm, NewsFormCreate


def home_page(request):
    news_all = News.objects.all()
    context = {"news": news_all}
    return render(request, "home.html", context)


def news_details_page(request, id):
    news_id = News.objects.get(id=id)
    context = {"news": news_id}
    return render(request, "news_details.html", context)


def category_form(request):
    if request.method == "POST":
        form_create = CreateForm(request.POST)
        if form_create.is_valid():
            form_create.save()
            return redirect("home-page")
    else:
        form_create = CreateForm()

    context = {"form": form_create}
    return render(request, "categories_form.html", context)


def news_form(request):
    categories = Categories.objects.all()
    if request.method == 'POST':
        form_news = NewsFormCreate(request.POST, request.FILES)
        if form_news.is_valid():
            form_news.save()
            return redirect('home-page')
    else:
        form_news = NewsFormCreate()

    context = {"form": form_news,
               'categories': categories}
    return render(request, 'news_form.html', context)
