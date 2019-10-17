
from django.db import models

# Create your models here.


class PostSession(models.Model):
    class Meta:
        verbose_name = 'session'
        verbose_name_plural = 'sessions'

    name = models.CharField(max_length=25)


class PostImage(models.Model):
    class Meta:
        verbose_name = 'photo'
        verbose_name_plural = 'photos'

    name = models.ForeignKey(
        PostSession, on_delete=models.CASCADE, null=True, blank=True)
    file = models.ImageField(upload_to='photos')
