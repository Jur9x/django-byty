from django.urls import path

from . import views

urlpatterns = [
    path('', views.BytListView.as_view(), name='index')
]