from django.shortcuts import render
from .models import Item, Topping
# Create your views here.
def kiosk(request):
    return render(request,'kiosk/kiosk.html')

def lotteria(request):
    items = Item.objects.filter().order_by('-pk') 
    return render(request,'kiosk/lotteria.html', {'items':items})