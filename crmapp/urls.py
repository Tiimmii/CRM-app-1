from django.urls import path
from . import views

app_name='leads'

urlpatterns = [
    path('leads-view/',views.view,name="view"),
]