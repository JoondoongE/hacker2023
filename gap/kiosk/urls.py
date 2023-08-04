from django.urls import path
from . import views

app_name = 'kiosk'
urlpatterns = [
    path('kiosk/',views.kiosk,name='kiosk'),
    path('lotteria/',views.lotteria,name='lotteria'),
]