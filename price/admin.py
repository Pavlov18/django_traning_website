from django.contrib import admin

# Зарегистрируем их в админке. Импортируем 2 класса.
from .models import PriceCard,  PriceTable

# Register your models here.
# И регистрируем 2 модели
admin.site.register(PriceCard)
admin.site.register(PriceTable)
