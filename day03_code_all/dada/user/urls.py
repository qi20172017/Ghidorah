from django.conf.urls import url
from . import views

urlpatterns = [
    #http://127.0.0.1:8000/v1/users
    url(r'^$', views.users),
    #http://127.0.0.1:8000/v1/users/activation?code=Z3VveGlhbzRfNDEwOQ==
    url(r'^/activation$', views.users_active)
]