from django.db import models

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from accounts.models import CustomUser


# Create your models here.

class News(models.Model):
    name = models.CharField(max_length=150, verbose_name='عنوان')
    content = RichTextUploadingField(blank=True , null=True , verbose_name="متن")
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='نویسنده', related_name='author')
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'news'

    def __int__(self):
        return self.id
