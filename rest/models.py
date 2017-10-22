# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Recharge (models.Model):
    first_name=models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    account_balance=models.IntegerField(default=0)

    def __str__(self):
       return self.first_name

    def get_absolute_url(self):
        return reverse ('mobile')