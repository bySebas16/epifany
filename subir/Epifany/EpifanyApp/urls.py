from django.urls import path

from EpifanyApp import views

urlpatterns = [
    path('', views.firstView, name="Home"),

]