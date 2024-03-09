from django.db import models


class Transportation_Air(models.Model):
    body = models.TextField(verbose_name='متن', blank=True)
    image = models.ImageField(default='avatar.jpg', upload_to="Transportation_Air/", verbose_name='تصویر', null=True,
                              blank=True)

    def __int__(self):
        return self.id


class Transportation_Maritime(models.Model):
    body = models.TextField(verbose_name='متن', blank=True)
    image = models.ImageField(default='avatar.jpg', upload_to="Transportation_Maritime/", verbose_name='تصویر',
                              null=True,
                              blank=True)

    def __int__(self):
        return self.id


class Transportation_Road(models.Model):
    body = models.TextField(verbose_name='متن', blank=True)
    image = models.ImageField(default='avatar.jpg', upload_to="Transportation_Road/", verbose_name='تصویر',
                              null=True,
                              blank=True)

    def __int__(self):
        return self.id


class Transportation_About(models.Model):
    body = models.TextField(verbose_name='متن', blank=True)

    def __int__(self):
        return self.id


class Transportation_Members(models.Model):
    fullname = models.TextField(verbose_name='نام و نام خانوادگی', blank=True)
    body = models.TextField(verbose_name='متن', blank=True)
    status = models.BooleanField(verbose_name='وضعیت')
    image = models.ImageField(default='avatar.jpg', upload_to="Transportation_Members/", verbose_name='تصویر',
                              null=True,
                              blank=True)

    def __int__(self):
        return self.id


class Transportation_Certificate(models.Model):
    name = models.TextField(verbose_name='نام و نام خانوادگی', blank=True)
    status = models.BooleanField(verbose_name='وضعیت')
    image = models.ImageField(default='avatar.jpg', upload_to="Transportation_Certificate/", verbose_name='تصویر',
                              null=True,
                              blank=True)

    def __int__(self):
        return self.id