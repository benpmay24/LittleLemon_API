from django.urls import include, path
from rest_framework import routers
from . import views


urlpatterns = [
    path("groups/manager/users/",views.ManagerGroupViewSet.as_view({'get': 'list', 'post': 'create', 'delete': 'destroy'})),
    path("groups/delivery-crew/users/",views.ManagerGroupViewSet.as_view({'get': 'list', 'post': 'create', 'delete': 'destroy'})),
    path("secret/",views.secret_message),
    path("users/",include("djoser.urls")),
    path("users/",include("djoser.urls.authtoken")),
]