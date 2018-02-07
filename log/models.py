# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from fibermotor.models import Region
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Log_type(models.Model):
    type = models.CharField(verbose_name='日志类型', null=True, max_length=40)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = '操作类型'
        verbose_name_plural = '操作类型'


@python_2_unicode_compatible
class Log(models.Model):
    title = models.CharField(verbose_name='标题', null=True, max_length=40)
    person = models.CharField(verbose_name='责任人', null=True, max_length=40)
    type = models.ForeignKey(Log_type, null=True, on_delete=models.PROTECT, verbose_name='日志类型')
    start_time = models.DateField(verbose_name='操作时间')
    update_time = models.DateField(verbose_name='更新时间', auto_now=True)
    region = models.ForeignKey(Region, null=True, on_delete=models.PROTECT, verbose_name=u'机房')
    detail = models.CharField(verbose_name='内容', null=True, max_length=40)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '日志内容'
        verbose_name_plural = '日志内容'