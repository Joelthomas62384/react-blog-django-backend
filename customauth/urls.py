from django.urls import path
from . import views
from . models import *

urlpatterns=[
     path('api/users/', views.RegisterUserListCreateView.as_view(), name='user-list-create'),
    path('api/users/<str:id>/', views.RegisterUserListCreateView.as_view(), name='user-detail-delete'),
]