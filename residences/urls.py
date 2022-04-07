from django.urls import path
from . import views

urlpatterns = [
    path('', views.HelloResidencesView.as_view(), name='hello_residences')
]
