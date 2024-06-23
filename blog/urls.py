from django.urls import path
from blog import views

app_name = "blog"

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contactt', views.contactt, name="contactt"),
]