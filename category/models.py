from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='نوع مشاوره')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'category'
        managed = True
        verbose_name = 'مشاوره'
        verbose_name_plural = 'مشاوره'