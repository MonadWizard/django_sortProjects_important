from django.urls import path
from todo import views

urlpatterns = [
    path('signup/', views.signupuser, name='signupuser' )


]
