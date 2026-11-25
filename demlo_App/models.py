from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
# from django.conf import settings 

# User = settings['AUTH_USER_MODEL']


class UserWithPhone(AbstractUser):
    phone = models.CharField("Номер телефона", max_length=15)
    def __str__(self):
        return self.username 
    
User = get_user_model()

class Service(models.Model):
    name = models.CharField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    comment = models.TextField('Комментарий')
    status = models.IntegerField(
        'Статус заявки',
        choices=[
        (1, 'Новая'),
        (2, 'Подтверждено'),
        (3, 'Выполнена'),
        ],
        default='new')
    created_at = models.DateTimeField("Дата создания", auto_now=True)
    class Meta:
        verbose_name = 'Заявка',
        verbose_name_plural = 'Заявки'
    