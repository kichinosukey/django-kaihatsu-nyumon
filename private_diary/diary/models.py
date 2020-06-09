from django.contrib.auth.models import User
from django.db import models


class Bmi(models.Model):
    """BMI宣言モデル"""

    user = models.ForeignKey(User, verbose_name='ユーザー', on_delete=models.PROTECT)
    bmi = models.FloatField(verbose_name='BMI', null=True, blank=True)
    comment = models.CharField(verbose_name='コメント', max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Bmi'

    def __str__(self):
        return self.created_at