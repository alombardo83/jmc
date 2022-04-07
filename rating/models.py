import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Rating(models.Model):
    username = models.CharField('nom d\'utilisateur', max_length=100)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    body = models.TextField('avis')
    date = models.DateTimeField('publié le', auto_now_add=True, editable=False)

    class Meta:
        ordering = ['-date']
        verbose_name = 'avis'
        verbose_name_plural = 'avis'

    def __str__(self):
        return '{} - {} - {}'.format(self.username, self.rating, self.date.strftime('%x %X'))


class Response(models.Model):
    rating = models.OneToOneField(
        Rating,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    body = models.TextField('réponse')
    date = models.DateTimeField('a répondu le', auto_now_add=True, editable=False)