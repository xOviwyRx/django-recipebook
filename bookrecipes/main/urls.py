from django.urls import path
from .views import recipes

app_name = 'main'
urlpatterns = [
    path("", recipes, name='recipes'),
]
