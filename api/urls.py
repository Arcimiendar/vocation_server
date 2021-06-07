from api.views import DestroySearchWordView, ListCreateSearchWordView
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('search_words/', ListCreateSearchWordView.as_view()),
    path('search_words/<str:pk>', DestroySearchWordView.as_view()),
    path('token/', obtain_auth_token)
]
