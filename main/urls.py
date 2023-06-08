from django.urls import path
from . import views

urlpatterns=[
  path("", views.index, name="index"),
  path("skills", views.skills, name="skills"),
  path("about", views.about, name="about"),
  path("products", views.products, name="products")
]