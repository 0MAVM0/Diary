from django.urls import path
from .views import *

urlpatterns= [
    path("", home_page, name="home"),
    path("sign_up/", SignUpView.as_view(), name="sign_up"),
    path("log_in/", log_in, name="log_in"),
    path("log_out/", log_out, name="log_out"),
    path("profile/<int:id>/", profile_view, name="profile"),
]
