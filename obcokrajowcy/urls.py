from django.urls import path, include
from .views import wszystkie_wpisy

urlpatterns = [
    path('', wszystkie_wpisy, name='wszystkie_wpisy'),
]