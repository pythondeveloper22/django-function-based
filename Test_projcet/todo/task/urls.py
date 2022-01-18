from django.urls import path
from . import views

urlpatterns = [

    path('studentinfo/',views.studentinfo)
]
