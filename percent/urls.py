from django.urls import path
from .views import index, home, converter

urlpatterns = [
    path('', home, name='home'),
    path('percent/', index, name='percent'),
    path('convert/', converter, name='convert'),
]
