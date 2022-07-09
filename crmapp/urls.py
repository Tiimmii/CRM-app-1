from django.urls import path
from . import views

app_name="leads"

urlpatterns = [
    path('leads-view/',views.view,name='view'),
    path('leads-details/<str:pk>/', views.details, name='details'),
    path('leads-create/', views.create, name='create'),
]