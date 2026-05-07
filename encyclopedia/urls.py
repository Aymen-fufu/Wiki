from django.urls import path,include
from . import views

app_name = "encyclopedia"
urlpatterns =[
    path("", views.index, name="index"),
    path("<str:name>", views.article, name="article")
]
