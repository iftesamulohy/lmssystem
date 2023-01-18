from django.urls import path
from lms import views

urlpatterns = [
    path("",views.ModulesApi.as_view()),
]
