from django.urls import path
from . import views



urlpatterns= [
    path('',views.UserGetView.as_view()),
    path('<int:id>/', views.UserDetails.as_view())
]