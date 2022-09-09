from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
import uuid


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    chat_id = models.PositiveIntegerField(
        verbose_name='Telegram ID',
        unique=True,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class UserLocation(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    location_uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        verbose_name='UUID локации',
        unique=True,
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Название локации'
    )
    address = models.CharField(
        max_length=255,
        verbose_name='Адрес'
    )
    status = models.CharField(
        max_length=16,
        verbose_name='Статус'
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления'
    )

    def __str__(self):
        return f"{self.title} | {self.user.username}"

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


class LocationCamera(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    location = models.ForeignKey(
        UserLocation,
        on_delete=models.CASCADE,
    )
    camera_uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        verbose_name='UUID камеры',
        unique=True,
    )
    video = models.FileField(
        default='',
        upload_to='accounts/camera_video',
        null=True,
        blank=True
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Название камеры'
    )
    status = models.CharField(
        max_length=16,
        verbose_name='Статус'
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления'
    )

    def __str__(self):
        return f"{self.title} | {self.user.username}"

    class Meta:
        verbose_name = 'Камера'
        verbose_name_plural = 'Камеры'


class CustomerDataRegistration(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    camera = models.ForeignKey(
        LocationCamera,
        on_delete=models.CASCADE,
    )
    count = models.PositiveIntegerField(
        verbose_name='Количество посетителей'
    )
    warning_flag = models.BooleanField(
        verbose_name='Нарушение',
        editable=True
    )
    date = models.DateTimeField(
        verbose_name='Время фиксации'
    )

    def __str__(self):
        return f"{self.camera.title} | Нарушения"

    class Meta:
        verbose_name = 'Регистрация посетителей'
        verbose_name_plural = 'Регистрация посетителей'
