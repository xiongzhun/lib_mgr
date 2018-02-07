# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Phone(models.Model):
    name = models.CharField(verbose_name='姓名', null=True, max_length=40)
    mail = models.EmailField(verbose_name='邮箱', max_length=80)
    phone = models.BigIntegerField(verbose_name='电话')
    update_time = models.DateField(verbose_name='更新时间', auto_now_add=True)
