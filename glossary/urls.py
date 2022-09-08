from django.urls import path
from . import views

urlpatterns = [
    path('', views.entries, name='glossary-entries'),
    path('<int:entry_id>/', views.entry, name='entry')
]