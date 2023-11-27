from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=10, unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=100, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=200,null=True, blank=True)
    is_published = models.BooleanField(default=False, blank=True)
    image = models.ImageField(upload_to="ads/", null=True, blank=True)



    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.name