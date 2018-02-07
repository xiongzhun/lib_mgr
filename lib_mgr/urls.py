from django.conf.urls import url
from django.contrib import admin
from fibermotor import views as lib_mgr
from web import views as web
from log import views as log
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^host/$', lib_mgr.host_listing),
    url(r'^host/(\d+)$', lib_mgr.host_detail, name='host-detail'),
    url(r'^host/unused/$', lib_mgr.host_unused),
    url(r'^host/no_time/$', lib_mgr.host_no_time),
    url(r'^host/out_time/$', lib_mgr.host_out_time),
    url(r'^host/always/$', lib_mgr.host_always),
    url(r'^host/active/$', lib_mgr.host_active),
    url(r'^search/$', lib_mgr.search, name='search'),
    url(r'^ip/$', lib_mgr.ip_listing, name='ip-list'),
    url(r'^ip/(\d+)$', lib_mgr.ip_detail, name='ip-detail'),
    url(r'^ip/unused/$', lib_mgr.ip_unused),
    url(r'^ip/no_time/$', lib_mgr.ip_no_time),
    url(r'^ip/out_time/$', lib_mgr.ip_out_time),
    url(r'^ip/always/$', lib_mgr.ip_always),
    url(r'^ip/active/$', lib_mgr.ip_active),
    url(r'^ip/$', log.log_listing, name='log'),
    url(r'^', web.index),
]

urlpatterns += static('/static/', document_root='/static/')