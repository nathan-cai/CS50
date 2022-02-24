from django.urls import path
from numpy import greater_equal
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("nathan", views.nathan, name="nathan"),
    path('<str:name>', views.greet, name='greet')
]
