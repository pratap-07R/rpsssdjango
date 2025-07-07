from django.urls import path

from . import views 
urlpatterns = [
    path("signup/",views.rpsSignupUser.as_view()),
    path("getAllUser/",views.rpsGetUserDetails.as_view()),
    path("updateEmail/", views.rpsUpdateEmail.as_view()),
    path("deleteUser/<number>/", views.rpsDeleteUser.as_view())
]