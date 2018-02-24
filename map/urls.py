from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('<int:map>/', views.index),
    path('<int:map>/edit/', views.edit),
    path('submit/node', views.submit_node),
    path('submit/edge', views.submit_edge),
    path('<int:map>/locations', views.update_locations),
]
