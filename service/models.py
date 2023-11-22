from django.db import models
from category.models import Category


class Service(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='نوع مشاوره')
    name = models.CharField(max_length=100, verbose_name='زمینه تخصص')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'service'
        managed = True
        verbose_name = 'تخصص'
        verbose_name_plural = 'تخصص'