from django.conf.urls import url,include
from . import views
urlpatterns = [  
    url(r'^SignUpSave/', views.SignUpSave, name="signupsave"),
    url(r'^console/', views.console, name="console"),
    url(r'^SignUp/', views.SignUp, name="signup"),
    url(r'^LogIn/', views.LogIn, name="login"),
    url(r'^LogOut/', views.logout, name="logout"),
    url(r'^$', views.Index, name="index"),
]