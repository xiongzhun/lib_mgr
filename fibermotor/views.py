# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from fibermotor import models


# Create your views here.


def host_listing(request):
    host_list = models.Computer.objects.all().order_by("mgr_ip")
    paginator = Paginator(host_list, 10)
    page = request.GET.get('page')
    try:
        host_list = paginator.page(page)
    except PageNotAnInteger:
        # 如果page不是整数，则展示第1页
        host_list = paginator.page(1)
    except EmptyPage:
        # 如果page超过范围，则展示最后一页
        host_list = paginator.page(paginator.num_pages)
    query_params = request.GET.copy()
    query_params.pop('page', None)  # delete page param
    context = {
        'page': page,
        'paginator': paginator,
        'query_params': query_params,
        'host_list': host_list,
    }

    return render(request, 'host_list.html', context)


def ip_listing(request):
    ip_list = models.Ips.objects.all().order_by("ip")
    paginator = Paginator(ip_list, 10)
    page = request.GET.get('page')
    try:
        ip_list = paginator.page(page)
    except PageNotAnInteger:
        # 如果page不是整数，则展示第1页
        ip_list = paginator.page(1)
    except EmptyPage:
        # 如果page超过范围，则展示最后一页
        ip_list = paginator.page(paginator.num_pages)
    query_params = request.GET.copy()
    ip_count = models.Ips.objects.count()
    query_params.pop('page', None)  # delete page param
    context = {
        'page': page,
        'paginator': paginator,
        'query_params': query_params,
        'ip_list': ip_list,
        'ip_count': ip_count,
    }
    return render(request, 'ip_list.html', context)


def host_detail(request, compter_id):
    try:
        p = models.Computer.objects.get(id=compter_id)
    except models.Computer.DoesNotExist:
        raise Http404("Computer does not exist")
    context = {
        'host_detail': p,
    }
    return render(request, 'host_detail.html', context)


def ip_detail(request, ips_ip):
    try:
        p = models.Ips.objects.get(id=ips_ip)
    except models.Ips.DoesNotExist:
        raise Http404("ip does not exist")
    context = {
        'ip_detail': p,
    }
    return render(request, 'ip_detail.html', context)


def search(request):
    q = request.GET.get('q')
    error_msg = 'none'

    if not q:
        error_msg = '请输入关键词'
        return render(request, 'errors.html', {'error_msg': error_msg})

    host_list = models.Computer.objects.filter(name__contains=q)
    paginator = Paginator(host_list, 10)
    page = request.GET.get('page')
    try:
        host_list = paginator.page(page)
    except PageNotAnInteger:
        # 如果page不是整数，则展示第1页
        host_list = paginator.page(1)
    except EmptyPage:
        # 如果page超过范围，则展示最后一页
        host_list = paginator.page(paginator.num_pages)
    query_params = request.GET.copy()
    query_params.pop('page', None)  # delete page param
    context = {
        'page': page,
        'paginator': paginator,
        'query_params': query_params,
        'host_list': host_list,
    }

    return render(request, 'results.html', context)