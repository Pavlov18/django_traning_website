from django.shortcuts import render
from .models import Order
from .forms import OrderForm
from cms.models import CmsSlider
from price.models import PriceCard, PriceTable

# Create your views here.
def first_page(request):
    slider_list = CmsSlider.objects.all()
    # Из класса PriceCard берем элементы по id через конструкцию GET с параметром id1 , 2 и 3
    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)
    # Из второго класса (pricetable) берем все элементы и передаём в рендер
    price_table = PriceTable.objects.all()
    # Передаём форму в словарь
    form = OrderForm()
    # Так как количество передаваемых объектов уже не малое, запишем их все в переменную (словарь) и передадим потом её вместо словаря (для красоты)
    dict_obj = {
        'slider_list': slider_list,
        'pc_1': pc_1,
        'pc_2': pc_2,
        'pc_3': pc_3,
        'price_table': price_table,
        'form': form,
    }
    return render(request, './index.html', dict_obj)

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