from django.urls import path
from votes import views

urlpatterns = [
    path('', views.VoteList.as_view()),
]
