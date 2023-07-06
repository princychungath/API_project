from django.urls import path
from api import  views

urlpatterns=[
    path('',views.ProfileCreateList.as_view(),name="profile-list"),
    path('<int:pk>',views.ProfileDetail.as_view(),name="profile-detail"),
]
