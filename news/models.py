from django.db import models
from django.urls import reverse

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from accounts.models import CustomUser


# Create your models here.

class News_Transportation(models.Model):
    name = models.CharField(max_length=150, verbose_name='عنوان')
    slug = models.SlugField()
    image = models.ImageField(default='avatar.jpg', upload_to="News/Transportation/", verbose_name='تصویر',
                              null=True,
                              blank=True)
    content = RichTextUploadingField(blank=True, null=True, verbose_name="متن")
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='نویسنده', related_name='author_user')
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'news_transportation'

    def __int__(self):
        return self.id