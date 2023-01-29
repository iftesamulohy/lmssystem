from django.urls import path
from lms import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'courses',views.ModulesApi,basename="module")
router.register(r'user',views.Userme,basename="user")
urlpatterns = [
    path('register/',views.RegisterUser.as_view()),
    
]
urlpatterns+= router.urls