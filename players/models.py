from django.db import models
from django.utils import timezone

class Player(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    age = models.PositiveIntegerField(verbose_name="Возраст")
    position = models.CharField(max_length=50, verbose_name="Позиция")
    height = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Рост (см)")
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Вес (кг)")
    image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name="Изображение")
    biography = models.TextField(blank=True, null=True, verbose_name="Биография")
    date_added = models.DateTimeField(default=timezone.now, verbose_name="Дата добавления")  # Поле для даты добавления

    def __str__(self):
        return self.name
