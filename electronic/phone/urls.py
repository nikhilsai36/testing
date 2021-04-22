from .views import *
from django.urls import path
from django.conf.urls import url


urlpatterns = [
    path('index/', index),
    path('register/', register),
    # path('create/', create),
    path('edit/<int:id>', edit),
    path('update/<int:id>', update),
    path('delete/<int:id>', delete1),
    path('login/', login),
    path('logout/', logout)
]


