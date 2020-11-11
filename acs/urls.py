from django.urls import path

from . import views
app_name = 'acs'

urlpatterns = [
    # Ex: localhost:7000
    path('', views.index, name='index'),

    # Ex: localhost:7000/auth
    path('auth/', views.auth, name='auth'),

    # Ex: localhost:7000/result
    path('result/', views.result, name='result'),
]
