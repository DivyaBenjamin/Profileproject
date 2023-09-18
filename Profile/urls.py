from django.urls import path
from Profile import views
app_name="Profile"
urlpatterns = [
    path('Profile/',views.Profile,name="Profile"),
]