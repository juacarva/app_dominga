from django.urls import path
from .views import home, detalle


urlpatterns = [
    path('', home, name='home'),
    path('detalle/<int:id>', detalle, name='detalle'),
]