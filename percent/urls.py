from django.urls import path
from .views import index, home

urlpatterns = [
    path('', home, name='home'),
    path('percent/', index, name='percent'),
]
