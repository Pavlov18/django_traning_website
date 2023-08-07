from django.db import models


# Create your models here.

# Пропишем статусы заявки
# Класс со статусами должен быть класса Order. Иначе поле СТАТУС не видит данный класс.
class StatusCrm(models.Model):
    status_name = models.CharField(max_length=200, verbose_name="Название статуса")

    def __str__(self):
        return self.status_name
    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"





class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name="Имя")
    order_phone = models.CharField(max_length=200, verbose_name="Телефон")

    # Создаем новое поле orders, прявязав поле к новому классу таким образом, что класс status становится родителем поля order_status. Указываем, что поле - это поле привязки, поэтому типа поля ForeignKey (внешний ключ)

    # Используем PROTECT, т.к. не хотим доавать пользователя удалять статусы.
    # null-true нужно для одобрения пустоты в БД, а blank=true для пустоты в полях админ-панели django
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Статус")



    def __str__(self):
        return self.order_name
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

# Комментарии (будут дочерним классом объекта класса order c полями "Дата создания" и "Текст комментария". Создаём класс Comment ниже класса Order
# on_delete=models.CASCADE - удаление по каскаду, что означает, что при удалении родителя (заказа) удалится и сам комментарий к нему.
class CommentCrm(models.Model):

    # Первым полем будет поле привязки. Так и назовём его binding.
    comment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Заявка")

#     Далее Поле комментария. Т.к. комментарий может быть очень длинным, то используем TextField вместо CharField.
    comment_text = models.TextField(verbose_name="Текст комментария")

#     Поле даты написания комментария
    comment_dt = models.DateTimeField(auto_now=True, verbose_name="Дата создания")

#     Строковым представлением пока выставим comment_text и добавим имена для объекта
    def __str__(self):
        return self.comment_text
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
    # После этого выведем модель CommentCrm в админку и потом произведем миграцию.