from django.urls import path


urlpatterns= [
    path('',views.UserGetView.as_view()),
    path('<int:id>/', views.UserDetails.as_view())
]