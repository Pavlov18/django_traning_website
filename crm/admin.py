from django.contrib import admin
from .models import Order, StatusCrm, CommentCrm
# Register your models here.

# Вывод комментария в карточку, чтобы не переходить из одной страницы в другую
class Comment(admin.StackedInline):
    model = CommentCrm
    fields = ('comment_dt', 'comment_text')
    readonly_fields = ('comment_dt',)
    # Делаем одно поле комментария в карточке, заместо 3 (extra = 1, по-умолчанию 3)
    extra = 1

# Кастомизируем админ-панель с помощью ModelAdmin
# Создаём класс, который наследуется от admin.ModelAdmin, который будет управлять полями вывода-ввода данных в админ панели
class OrderAdm(admin.ModelAdmin):
    # list_display содержить кортеж с именами полей из модели, которые мохим отобразить в таблице в админ-панели
    list_display = ('id', 'order_status', 'order_name', 'order_phone', 'order_dt',)

    # Сделаем кликабельным в Заказах еще и Имя помимо Id
    list_display_links = ('id', 'order_name',)

    # Поле search_fields позволяет искать данные по полям из кортежа
    search_fields = ('id', 'order_name', 'order_phone', 'order_dt',)

    # Сделаем фильтр по статусу заказа
    list_filter = ('order_status',)

    # Позволяет редактировать поля, не заходя в саму карточку, прямо в таблице
    list_editable = ('order_status', 'order_phone')

    # Добавление пагинации на страницу
    list_per_page = 10
    list_max_sho_all = 100

    # Настройка карточек Порядок полей.
    fields = ('id', 'order_status', 'order_dt', 'order_name', 'order_phone')
    readonly_fields = ('id', 'order_dt')

    # Вывод комментария в карточку, чтобы не переходить из одной страницы в другую
    # поле класса комент
    inlines = [Comment, ]

# Теперь передадим в регистр данный класс (OrderAdm) как второй аргумент к уже существующему классу Order
admin.site.register(Order, OrderAdm)
admin.site.register(StatusCrm)
admin.site.register(CommentCrm)