from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('project/new', views.add_new_project, name='add_new_project')
]
