from django.urls import path

#views
from . import views

#Django setting

#config URL
urlpatterns = [
    path('', views.profile, name="profile"),
]