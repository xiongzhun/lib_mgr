# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Region(models.Model):
    name = models.CharField(verbose_name='主机名', null=True, max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '机房'
        verbose_name_plural = '机房'


@python_2_unicode_compatible
class Computer(models.Model):
    sn = models.CharField(verbose_name='SN序号', max_length=20)
    name = models.CharField(verbose_name='主机名', blank=True, max_length=40)
    purpose = models.CharField(verbose_name='使用目的', default='无', max_length=80)
    person = models.CharField(verbose_name='负责人', default='无', max_length=20)
    always = models.BooleanField(verbose_name='长期占用')
    left_time = models.IntegerField(verbose_name='剩余天数', default='0')
    update_time = models.DateField(verbose_name='更新时间', auto_now=True)
    region = models.ForeignKey(Region, null=True, on_delete=models.PROTECT, verbose_name=u'机房')
    area = models.CharField(verbose_name='区域', max_length=20)
    cabinet = models.CharField(verbose_name='机柜', max_length=20)
    bmc_ip = models.GenericIPAddressField(verbose_name='BMC IP')
    mgr_ip = models.GenericIPAddressField(verbose_name='管理 IP')
    cpu = models.CharField(verbose_name='CPU', blank=True, max_length=20)
    RAM = models.CharField(verbose_name='内存', blank=True, max_length=20)
    disk = models.CharField(verbose_name='存储', blank=True, max_length=20)
    mac_0 = models.CharField(verbose_name='网卡1 MAC 地址', blank=True, max_length=20)
    mac_1 = models.CharField(verbose_name='网卡2 MAC 地址', blank=True, max_length=20)
    mac_2 = models.CharField(verbose_name='网卡3 MAC 地址', blank=True, max_length=20)
    mac_3 = models.CharField(verbose_name='网卡4 MAC 地址', blank=True, max_length=20)

    def __str__(self):
        return self.sn

    class Meta:
        verbose_name = '服务器'
        verbose_name_plural = '服务器'


class Ips(models.Model):
    ip = models.GenericIPAddressField(verbose_name='IP 地址')
    person = models.CharField(verbose_name='负责人', max_length=20)
    purpose = models.CharField(verbose_name='使用目的', default='无', max_length=20)
    always = models.BooleanField(verbose_name='长期占用')
    left_time = models.IntegerField(verbose_name='剩余天数', default='0')
    update_time = models.DateField(verbose_name='更新时间', auto_now=True)
    bmc_ip = models.BooleanField(verbose_name='是否BMC')

    def __str__(self):
        return self.ip

    class Meta:
        verbose_name = 'ip'
        verbose_name_plural = 'ip'
