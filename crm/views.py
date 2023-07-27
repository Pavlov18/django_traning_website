from django.shortcuts import render
from .models import Order
from .forms import OrderForm

# Create your views here.
def first_page(request):
    object_list = Order.objects.all()
    form = OrderForm()
    return render(request, './index.html', {'object_list': object_list,'form': form})

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