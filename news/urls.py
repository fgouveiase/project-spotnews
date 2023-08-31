from news.views import home_page, news_details_page, category_form
from django.urls import path


urlpatterns = [
    path("", home_page, name="home-page"),
    path("news/<int:id>", news_details_page, name="news-details-page"),
    path("categories", category_form, name="categories-form"),
]
