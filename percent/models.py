from django.db import models


class Percent(models.Model):
    number = models.PositiveBigIntegerField()
    percent = models.PositiveBigIntegerField()
    percent_value = models.PositiveBigIntegerField()
    residual_value = models.PositiveBigIntegerField()
    value_increase = models.PositiveBigIntegerField()

    def __str__(self):
        return self.number
