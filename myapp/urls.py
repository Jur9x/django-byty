from django.urls import path

from . import views

urlpatterns = [
    path('', views.NemovitostList.as_view(), name='index'),
    path('detailn.html/<int:pk>/', views.NemovitostDetailView.as_view(), name='detailn'),
    path('detailo.html/<int:pk>/', views.OsobaDetailView.as_view(), name='detailo')
]