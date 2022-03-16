from django.urls import path

#views
from . import views

#config URL
urlpatterns = [
    path('', views.profile, name="profile"),
]