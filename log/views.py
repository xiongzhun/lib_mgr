# -*- coding: utf-8 -*-
from django.shortcuts import render
from log import models
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
# Create your views here.


def log_listing(request):
    log_list = models.Log.objects.all().order_by('start_time')
    paginator = Paginator(log_list, 10)
    page = request.GET.get('page')
    try:
        log_list = paginator.page(page)
    except PageNotAnInteger:
        # 如果page不是整数，则展示第1页
        log_list = paginator.page(1)
    except EmptyPage:
        # 如果page超过范围，则展示最后一页
        log_list = paginator.page(paginator.num_pages)
    query_params = request.GET.copy()
    query_params.pop('page', None)  # delete page param
    context = {
        'page': page,
        'paginator': paginator,
        'query_params': query_params,
        'log_list': log_list,
    }

    return render(request, 'log_list.html', context)