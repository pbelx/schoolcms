from django.urls import path
from . import views

urlpatterns = [
    path("x", views.hello, name='hello'),
    path("", views.index, name='home'),
    path("details/", views.detail, name='details'),
    path("<int:questionid>/results", views.result, name='results'),
    path("<int:questionid>/vote", views.vote, name='vote'),
    path("<int:questionid>/details", views.details, name='details'),

]
