from django.shortcuts import render
from .models import Order
from .forms import OrderForm
from cms.models import CmsSlider

# Create your views here.
def first_page(request):
    slider_list = CmsSlider.objects.all()
    form = OrderForm()
    return render(request, './index.html', {'slider_list': slider_list,})

# Создаём функцию, которая выводит html страницу Спасибо
def thanks_page(request):
    # Получение данных из запроса
    name = request.POST['name']
    phone = request.POST['phone']

    # Сохранене данных в базу данных. Создаем экземляр класса и методом save сохраняем запрос в БД
    element = Order(order_name=name, order_phone=phone)
    element.save()

    return render(request, './thanks_page.html',{
        'name':name,
        'phone':phone
        })